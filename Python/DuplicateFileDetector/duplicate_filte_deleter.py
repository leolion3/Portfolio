#!/usr/bin/env python3
import os
import difflib
import json
from pathlib import Path
from string import punctuation


def get_all_files(directory):
    """
    Recursively gets all files in the given directory and its subdirectories.
    
    :param directory: The root directory to start the search from.
    :return: A list of file paths.
    """
    files_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            files_list.append(os.path.join(root, file))
# ---------------------------------------------------------------------------------
#           TODO if you want file extensions, remove previous line and comment in:
#            if file.endswith('.mp3'):
#                files_list.append(os.path.join(root, file))
    return files_list


def clean_name(filename):
    """
    Clean file name of gunk like extensions and various irrelevant symbols to increase
    statistical likelihood of finding actual similarities.
    
    :param filename: name of the file.
    :return: cleaned filename
    """
    filename = Path(filename).stem
    filters = list(set(punctuation))
    for sym in filters:
        filename = filename.replace(sym, '')
    filename = ' '.join(filter(lambda x: len(x) > 0, filename.split(' ')))
    return filename


def find_similar_files(files, similarity_threshold=0.9):
    """
    Finds and lists pairs of files with similar names.
    
    :param files: List of file paths.
    :param similarity_threshold: The threshold above which files are considered similar.
    :return: A list of tuples, each containing two similar file paths.
    """
    similar_files = []
    for i in range(len(files)):
        for j in range(i + 1, len(files)):
            name1 = clean_name(os.path.basename(files[i]))
            name2 = clean_name(os.path.basename(files[j]))
            similarity = difflib.SequenceMatcher(None, name1, name2).ratio()
            if similarity > similarity_threshold:
                similar_files.append((files[i], files[j], similarity))
    return similar_files


def prompt_user_for_deletion(similar_files):
    """
    Prompts the user to decide which of the similar files to delete.
    
    :param similar_files: List of tuples containing pairs of similar file paths and their similarity score.
    """
    for file1, file2, similarity in similar_files:
        print(f"\nSimilarity: {similarity * 100:.2f}%")
        print(f"1: {file1}")
        print(f"2: {file2}")
        choice = input("Enter the number of the file to delete (or 's' to skip): ")
        if choice == '1':
            os.remove(file1)
            print(f"Deleted: {file1}")
        elif choice == '2':
            os.remove(file2)
            print(f"Deleted: {file2}")
        else:
            print("Skipped")


if __name__ == "__main__":
    directory = input("Enter the directory to search for duplicate files: ")
    files = get_all_files(directory)
    similar_files = find_similar_files(files)
    if similar_files:
        prompt_user_for_deletion(similar_files)
    else:
        print("No similar files found.")
