import mob
from db import load_reports

if __name__ == "__main__":
    mob.upload_file()
    mob.scan_file()
    load_reports()


    #mob.generate_pdf()