import os
import time
import getpass
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# 🔹 사용자 입력 (ID & Password)
user_id = input("📝 Enter your ID: ")
user_pw = getpass.getpass("🔒 Enter your Password: ")  # 입력할 때 화면에 보이지 않음

# 🔹 ChromeDriver 실행
print("🔹 ChromeDriver 실행 중...", flush=True)
service = Service("C:/chromedriver-win64/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # 🔹 창을 실행할 때 자동으로 최대화

driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()  # 🔹 실행 후 강제 최대화

# 🔹 Selenium 탐지 방지
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
})

# 🔹 웹사이트 접속
print("🔹 웹사이트 접속 중...", flush=True)
driver.set_page_load_timeout(10)
driver.get("http://ytams.yura.co.kr/")

# 🔹 페이지 로딩 대기
print("🔹 페이지 로딩 대기 중...", flush=True)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
print("✅ 페이지 로딩 완료!", flush=True)

# 🔹 로그인 과정
try:
    id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "mberId")))
    pw_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
    
    driver.execute_script("arguments[0].value = arguments[1];", id_input, user_id)
    driver.execute_script("arguments[0].value = arguments[1];", pw_input, user_pw)

    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="compose"]'))
    )
    driver.execute_script("arguments[0].click();", login_button)
    print("✅ 로그인 성공!")
except:
    print("❌ 로그인 실패!")
    driver.quit()
    exit()

# 🔹 로그인 후 페이지 로딩 대기
print("🔹 로그인 후 페이지 로딩 중...", flush=True)
time.sleep(3)

# 🔹 첫 번째 메뉴 클릭
try:
    menu1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="sidebarnav"]/li[3]/a'))
    )
    driver.execute_script("arguments[0].click();", menu1)
    print("✅ 첫 번째 메뉴 클릭 완료!")
except:
    print("❌ 첫 번째 메뉴 클릭 실패!")

# 🔹 두 번째 메뉴 클릭
try:
    menu2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="sidebarnav"]/li[3]/ul/li[1]/a'))
    )
    driver.execute_script("arguments[0].click();", menu2)
    print("✅ 두 번째 메뉴 클릭 완료!")
except:
    print("❌ 두 번째 메뉴 클릭 실패!")

# 🔹 데이터 로딩 대기
print("🔹 데이터 로딩 중...", flush=True)
time.sleep(3)

# 🔹 `tbody` 내 모든 `tr` 찾기
try:
    rows = driver.find_elements(By.XPATH, '//*[@id="listForm"]/div[2]/div/div/b/b/b/table/tbody/tr')
    print(f"✅ 감지된 행 개수: {len(rows)}")

    extracted_data = []
    
    for row in rows:
        first_td = row.find_element(By.TAG_NAME, "td")  # 첫 번째 <td> 요소 가져오기

        # 🔹 colspan="6"이 있는 행 제외
        if "colspan" in first_td.get_attribute("outerHTML") and 'colspan="6"' in first_td.get_attribute("outerHTML"):
            print("❌ colspan=6이 있는 행 건너뜀")
            continue

        # 🔹 6번째~10번째 td만 선택
        tds = row.find_elements(By.TAG_NAME, "td")[3:10]
        row_data = [td.text.strip() for td in tds]
        extracted_data.append(row_data)

    # 🔹 데이터 출력
    print("\n🔹 **추출된 데이터:**")
    for i, row in enumerate(extracted_data, start=1):
        print(f"{i}. {row}")

    print("✅ 데이터 추출 완료!")

except:
    print("❌ 데이터 추출 실패!")

# 🔹 자동 종료 방지
input("브라우저를 닫으려면 엔터를 누르세요...")

driver.quit()
