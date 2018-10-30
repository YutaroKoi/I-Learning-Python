# coding=utf-8
import hashlib

def bmi(h,w):
	"""
	身長と体重からBMIを算出する
	"""
	height=h/100
	weight=w
	return weight / (height * height)

def obesity_degree(bmi):
	"""
	BMIの値から肥満度を判定する
	闘値参照元：http://www.koshikijima.net/health/bmi-check.html
	"""
	bmi = float(bmi)

	if bmi > 25:
		return '太りすぎ'
	elif 24.2 <= bmi <= 25:
		return '太りぎみ'
	elif bmi < 18:
		return 'やせすぎ'
	else:
		return '標準'

def blood_pressure(high_pressure, low_pressure):
	"""
	最高血圧/最低血圧の値から血圧の状態を判定する
	闘値参照元：https://www.jpnsh.jp/data/jsh2014/jsh2014_gen.pdf
	"""
	high_pressure = float(high_pressure)
	low_pressure = float(low_pressure)

	if high_pressure >= 140 or low_pressure >= 90:
		return '高血圧'
	elif 130 <= high_pressure <= 139 or 85 <= low_pressure <= 89:
		return '正常高値血圧'
	elif 120 <= high_pressure <= 129 or 80 <= low_pressure <= 84:
		return '正常血圧'
	elif high_pressure < 129 and 80 < low_pressure:
		return '至適血圧'

def sqlite2google(date):
	"""
	sqlite3で保存した日付のフォーマットを
	Google Chartsの日付のフォーマットに変換する
	"""
	[yyyy,mm,dd]=date.split('-',)
	#Google Chartでは月の値を１減算
	mm = str(int(mm)-1)
	if len(mm)==1:
		mm='0'+mm
	return ','.join([yyyy,mm,dd])

def sqlite2fmt(date,sep='/'):
	"""
	sqlite3で保存した日付のフォーマットを
	引数sepで渡された区切り文字に置換する
	"""
	[yyyy,mm,dd]=date.split('-',)
	if len(mm)==1:
		mm='0'+mm
	return sep.join([yyyy,mm,dd])


def getdigest(password,account_id):
	"""
	パスワードをハッシュにする
	"""
	salt='&sf)b4nv0(%I'
	#ソルトを加える
	digest=salt+str(account_id)+password
	#ストレッチを１０回実施
	for i in range(10):
		digest = hashlib.sha256(digest).hexdigest()
	return digest

def is_password_ok(password, account_id, digest):
	"""
	パスワードの一致比較
	"""
	if digest == getdigest(password,account_id):
		return True
	else:
		return False
