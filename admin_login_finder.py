import requests

def find_admin_login_page(url):
    # List of common admin login page paths
    admin_paths = [
        "admin",
        "admin/login",
        "adminpanel",
        "administrator",
        "wp-admin",
        "wp-login.php",
        "login",
        "manager",
        "webadmin",
        "controlpanel",
        "cpanel",
        "admincp",
        "admin_area",
        "backend",
        "admin/login.php",
        "admin/index.php",
        "admin/admin.php",
        "admin_area/admin.php",
        "admin_area/login.php",
        "panel-administracion",
        "admin/admin_login.php",
        "admin_login",
        "admin1",
        "admin2",
        "admin3",
        "admin4",
        "admin5",
        "usuarios/login",
        "user/login",
        "user/admin",
        "admin_area/index.php",
        "admin_area/admin.html",
        "admin/account.php",
        "admin_area/login.html",
        "admin_area/index.html",
        "admin/cp.php",
        "cp.php",
        "administrator/index.php",
        "administrator/login.php",
        "administrator/account.php",
        "administrator.php",
        "login.php",
    ]

    found = False

    for path in admin_paths:
        full_url = f"{url}/{path}"
        try:
            response = requests.get(full_url, timeout=5)
            if response.status_code == 200:
                print(f"[+] Found: {full_url}")
                found = True
        except requests.exceptions.RequestException as e:
            print(f"[-] Error: {e}")

    if not found:
        print("[-] No admin login page found.")

if __name__ == "__main__":
    target_url = input("Enter the target URL (e.g., http://example.com): ").strip()
    find_admin_login_page(target_url)
