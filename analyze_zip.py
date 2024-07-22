import zipfile
import os
import shutil

def extract_zip(zip_path, extract_to='extracted'):
    """
    Extract the contents of the zip file to the specified directory.
    """
    if os.path.exists(extract_to):
        shutil.rmtree(extract_to)  # Remove the existing directory
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    return extract_to

def analyze_files(directory):
    """
    Analyze the files in the extracted directory and gather module, class, and function information.
    """
    analysis = {'modules': {}}
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                module_name = os.path.relpath(file_path, directory).replace(os.sep, '.').replace('.py', '')
                analysis['modules'][module_name] = {'classes': [], 'functions': []}
                for line in lines:
                    if line.strip().startswith('class '):
                        class_name = line.strip().split(' ')[1].split('(')[0]
                        analysis['modules'][module_name]['classes'].append(class_name)
                    elif line.strip().startswith('def '):
                        function_name = line.strip().split(' ')[1].split('(')[0]
                        analysis['modules'][module_name]['functions'].append(function_name)
    return analysis

def write_analysis_to_file(analysis, output_file):
    """
    Write the analysis results to a text file.
    """
    with open(output_file, 'w') as f:
        f.write("Analysis Results:\n")
        f.write("Modules and their contents:\n")
        for module, contents in analysis['modules'].items():
            f.write(f"\nModule: {module}\n")
            f.write(f"  Classes: {contents['classes']}\n")
            f.write(f"  Functions: {contents['functions']}\n")

def main():
    zip_path = 'invest.zip'  # Replace with your zip file name
    extract_to = 'extracted'
    output_file = 'code_summary.txt'

    # Step 1: Extract the ZIP file
    extracted_dir = extract_zip(zip_path, extract_to)

    # Step 2: Analyze the extracted files
    analysis = analyze_files(extracted_dir)

    # Step 3: Write the analysis results to a file
    write_analysis_to_file(analysis, output_file)

    # Step 4: Remove the extracted directory
    shutil.rmtree(extracted_dir)

    print(f"Analysis complete. Results written to {output_file}")

if __name__ == "__main__":
    main()
