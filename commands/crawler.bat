/home/ec2-user/workspace/dropbi/scripts/crawler-env/bin/python3 -m pip install --upgrade pip
@REM  install scrapy
conda install -c conda-forge scrapy
@REM create env
python3 -m venv crawler-env
@REM Start env
cd /d D:\Projetos\C4W\DropBi\scripts
#windows
crawler-env\Scripts\activate.bat
#linux
source crawler-env/bin/activate
@REM End env
deactivate
@REM run spider
scrapy crawl [spider] -O products\[file.json]