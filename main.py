from ip2geotools.databases.noncommercial import DbIpCity

# لیست آدرس‌های IP
ip_list = [
    '35.190.247.0',
    '35.191.0.0',
    '64.233.160.0',
    '35.190.247.0',
    '35.191.0.0',
    '64.233.160.0',
    '66.102.0.0',
    '66.249.80.0',
    '72.14.192.0',
    '74.125.0.0',
    '108.177.8.0',
    '108.177.96.0',
    '130.211.0.0',
    '172.217.0.0',
    '172.217.32.0',
    '172.217.128.0',
    '172.217.160.0',
    '172.217.192.0',
    '172.253.56.0',
    '172.253.112.0',
    '173.194.0.0',
    '209.85.128.0',
    '216.58.192.0',
    '216.239.32.0',
]

# تابع برای دریافت کشور از آدرس IP
def get_country(ip_address):
    try:
        response = DbIpCity.get(ip_address, api_key='free')
        return response.country
    except Exception as e:
        return "خطا: نمی‌توان اطلاعات را برای IP مورد نظر پیدا کرد."

# چاپ کشور برای هر آدرس IP در لیست
for ip in ip_list:
    country = get_country(ip)
    print(f'IP: {ip} -> کشور: {country}')
