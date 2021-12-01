# AWS instructions 

- If working on a existing EC2 instance, will need to go to EC2 dashboard and open port 8501 in the security settings 

- Update 
  - sudo apt-get update 
  - Test python is installed: e.g., type this in terminal: `python3` 
  - Install pip3 -> `sudo apt install python3-pip` 
  - Install streamlit -> `pip3 install streamlit`
  - Add to .bashrc file -> `nano ~/.bashrc` 
      - `export PATH="$HOME/.local/bin:$PATH"` to the very last line 
      - save / exit 
  - Then restart terminal -> `source ~/.bashrc` 
  - Then try `streamlit` in the terminal 

- Download github files 
  - git clone https://github.com/hantswilliams/AHI_STATS_507.git 

- Navigate to file: 
   - `/home/ubuntu/AHI_STATS_507/Week13_Summary` 
   - The file: `week13_streamlit.py` 

- Then run that streamlit: 
  - `streamlit run week13_streamlit.py`

- Need to then ensure all the python packages are available: 
  - example: 
    - `pip3 install pandas` 
    - ....`pip3 install {insertnamehere}` 