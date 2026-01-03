import unicodedata
import os
import glob

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)])

def process_directory(input_dir, output_file):
    words = set()
    # Find all .txt files in the input directory
    input_files = glob.glob(os.path.join(input_dir, "*.txt"))
    
    if not input_files:
        print(f"No .txt files found in {input_dir}")
        return

    for input_f in input_files:
        print(f"Processing {os.path.basename(input_f)}...")
        with open(input_f, 'r', encoding='utf-8') as f:
            for line in f:
                word = line.strip().upper()
                # Remove Greek accents
                word = remove_accents(word)
                # Handle precomposed accented Greek chars
                word = word.replace('Ά', 'Α').replace('Έ', 'Ε').replace('Ή', 'Η').replace('Ί', 'Ι').replace('Ό', 'Ο').replace('Ύ', 'Υ').replace('Ώ', 'Ω')
                word = word.replace('Ϊ', 'Ι').replace('Ϋ', 'Υ')
                word = word.replace('ς', 'Σ')
                
                cleaned_word = "".join([c for c in word if '\u0391' <= c <= '\u03AB'])
                
                if cleaned_word:
                    words.add(cleaned_word)
    
    sorted_words = sorted(list(words))
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for word in sorted_words:
            f.write(word + '\n')
    
    print(f"Successfully merged {len(input_files)} files into {output_file}.")
    print(f"Total unique words: {len(sorted_words)}")

if __name__ == "__main__":
    input_directory = "dicts"
    output_filename = "customdictionary.txt"
    
    if os.path.isdir(input_directory):
        process_directory(input_directory, output_filename)
    else:
        print(f"Directory '{input_directory}' not found. Please create it and add your .txt word lists.")
