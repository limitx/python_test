#include "Utils.h"
#include <unistd.h>
#include <errno.h> 

int debug1 = 0;
int debug2 = 0;

vector<string> key_tmp;
void Utils::loadkeys() {
	cout << "loadkeys\n";
	string strr;
    /*
    ifstream filein("./res/keywords.txt");

	while (getline(filein, str)) {
		if(str.length() > 0) {
			cout<<" keys "<<str<<endl;
			key_tmp.push_back(str);
		}
	}*/

	ifstream filein("./res/keys_src.txt");
	getline(filein, strr);

	cout<<" key src: "<<strr<<endl;

	const char *str = strr.c_str();
    do{
        const char *begin = str;

        while(*str != '|' && *str)
            str++;

		string tmp = string(begin, str);
		key_tmp.push_back(tmp);
		if (debug2 == 1) {
			cout << " key: " << tmp << endl;
		}
    } while (0 != *str++);
}

vector<string> files;
void Utils::loadfile(){
	// Direction
	DIR *dp;
	struct dirent *dirp;

	// Current working path
	char cwd[80];
	char *currentDir = getcwd(cwd, sizeof(cwd));

	if((dp = opendir(currentDir)) == NULL){
		cout << "Error(" << errno << ") opening " << currentDir << endl;
	}
	while((dirp = readdir(dp)) != NULL){
		string tmp = string(dirp->d_name);
		if(tmp.find(".txt") != string::npos) {
			files.push_back(tmp);
			cout << " files: " << tmp << endl;
		} else if(debug1){
			cout << tmp << endl;
		}
	}
	closedir(dp);
}

void Utils::search() {
	//const string key_tmp[] = {"imsmanager", " onfeat"};
	//const string key_tmp[] = {"//05"};
	
	for(int i = 0; i < files.size(); i++) {
		if (debug1) {
			cout << files[i] << endl;
		}
	 	ifstream filein(files[i]);
	 	ofstream fileout("tmp.txt");
		string str; 
		string regular_str;
		while (getline(filein, str)) {
			regular_str = str;
			transform(str.begin(), str.end(), str.begin(), ::tolower);

			for (string strr : key_tmp) {
				if(str.find(strr) != string::npos) {
					//string wordToReplace =regular_str.insert(0, "==");
					//size_t len = wordToReplace.length();
					//regular_str.replace(0, len, wordToReplace);
					fileout <<"++ "<< regular_str << endl;
				}
			}
	    }
		filein.close();
	}
}

extern "C" {
    Utils* Utils_new(){ return new Utils(); }
    void loadkeys(Utils* utils) { utils->loadkeys(); }
    void loadfile(Utils* utils) { utils->loadfile(); }
    void search(Utils* utils) { utils->search(); }
}
