#!/usr/bin/python3

import argparse
import os

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description="Hello young man! this app takes a path of folder or file and calculates its size in KB. hope you'll like it :D")
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-d", action="store_true", help="Path of a folder")
    group.add_argument("-f", action="store_true", help="Path of a file")
    
    parser.add_argument("-F", help="Enter a file format for your search. (example: txt) ")

    parser.add_argument("path", help="Enter the path you want to run the program in")
    
    args = parser.parse_args()
    
    # print(args.F, args.d, args.f, args.path)
    
    # -d
    if args.d  and not args.F and os.path.isdir(args.path):
        def getFolderSize(folder):
            total_size = os.path.getsize(folder)
            for item in os.listdir(folder):
                itempath = os.path.join(folder, item)
                if os.path.isfile(itempath):
                    total_size += os.path.getsize(itempath)
                elif os.path.isdir(itempath):
                    total_size += getFolderSize(itempath)
            return total_size
        
        print(getFolderSize(args.path)/1024, 'KB')
        
        # 1 level depth
        # def get_dir_size(path):
        #     total_size = 0
        #     for dirpath, dirnames, filenames in os.walk(path):
        #         for f in filenames:
        #             fp = os.path.join(dirpath, f)
        #             # skip if it is symbolic link
        #             if not os.path.islink(fp):
        #                 total_size += os.path.getsize(fp)
        #     return total_size
        
        # print(get_dir_size(args.path)/1024, 'KB')
        

    # -f
    elif args.f and not args.F and not os.path.isdir(args.path):
        print(os.path.getsize(args.path)/1024,'KB')
        
        
    # -F    
    elif args.d  and args.F and os.path.isdir(args.path):
        def get_size(path):
            total_size = 0
            for dirpath, dirnames, filenames in os.walk(path):
                for f in filenames:
                    if f.endswith(args.F):
                        fp = os.path.join(dirpath, f)
                        # skip if it is symbolic link
                        if not os.path.islink(fp):
                            total_size += os.path.getsize(fp)
            return total_size
        
        print(get_size(args.path)/1024, 'KB')
    
    else:
        print("please enter a valid input.\nuse --help to learn more.")
        
        


    