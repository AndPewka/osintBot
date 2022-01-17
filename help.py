def trans_tele(text):
	new_text = ""
	for i in range(len(text)):
		if text[i:i+1].isdigit():
			new_text = new_text + text[i:i+1]
	if new_text[0:1] == "7":
		new_text = new_text.replace("7","8",1)
	return new_text