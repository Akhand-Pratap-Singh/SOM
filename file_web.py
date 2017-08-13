from urllib import request

goog_url = 'url'

def download_any_file(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'file_name_u_wish_to_save.csv'
    fx = open(dest_url,"w")
    for line in lines:
        fx.write(line + "\n")

    fx.close()


download_any_file(goog_url)





