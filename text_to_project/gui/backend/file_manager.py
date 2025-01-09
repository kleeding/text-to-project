from os import listdir, remove
from os.path import isfile, join

class FileManager():
    def __init__(self, project_path):
        self.project_path = project_path

        self.file_names = self.get_files()

        # self.load_file('Calculator.txt') ## Load an initial file?? First in list

    def get_files(self):
        file_names = []
        names = listdir(self.project_path)

        for i in range(len(names)):
            if isfile(join(self.project_path, names[i])):
                file_names.append(names[i].replace(".txt",""))
            
        return file_names
    
    def get_names(self):
        return self.file_names
    
    def load_file(self, file_name):     
        txt = []
        with open(join(self.project_path, file_name),'r') as file:
            for line in file:
                txt.append(line)
        return txt
    
    def create_file(self, file_name):
        file = open(join(self.project_path, file_name + ".txt"), 'w')
        file.close()
        self.file_names.append(file_name)
        self.file_names = sorted(self.file_names)

    def save_file(self, file_name, contents):
        self.delete_file(file_name)
        with open(join(self.project_path, file_name + ".txt"), 'w') as file:
            for line in contents:
                file.write(line)

    def delete_file(self, file_name):
        if file_name in self.file_names:
            self.file_names.remove(file_name)
            remove(join(self.project_path, file_name + ".txt"))