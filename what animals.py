
print("")
print("")
print("   ██████╗    ██████╗     ███████╗")
print("  ██╔════╝    ██╔══██╗    ██╔════╝")
print("  ██║         ██████╔╝    █████╗  ")
print("  ██║         ██╔═══╝     ██╔══╝  ")
print("  ╚██████╗    ██║         ███████╗")
print("   ╚═════╝    ╚═╝         ╚══════╝")
print("")

# สร้างตัวแปร
global KB
global input_fact
global BlackBoard
global StartingNode
global TherminalNode
global inThen
global FireTheRule
global ThenPart
global Concluding

# กำหนดค่า

FireTheRule = False
debug = True
input_fact = True
inThen = 0
ThenPart = []
Concluding = []

KB = []
# Knowledge
Knowledge = [

    #อย่าเปลี่ยน / แก้ไข / ลบ / เพิ่ม กฎแล้วนะ เอาไปวาด Tree แล้ว
    'if อยู่บนบก and ออกลูกเป็นตัว Then สัตว์เลี้ยงลูกด้วยน้ำนม',
    'if สัตว์เลี้ยงลูกด้วยน้ำนม and มีงา and มีงวง Then ช้าง',
    'if สัตว์เลี้ยงลูกด้วยน้ำนม and มีกระเป๋าหน้าท้อง and กระโดดได้ and สีน้ำตาลอ่อน Then จิงโจ้',
    'if สัตว์เลี้ยงลูกด้วยน้ำนม and เชื่องช้า and สีน้ำตาลอ่อน and อาศัยอยู่บนต้นไม้ Then สลอธ',
    'if สัตว์เลี้ยงลูกด้วยน้ำนม and หูยาว and หางกลมสั้น and กินพืช Then กระต่าย',
    'if สัตว์เลี้ยงลูกด้วยน้ำนม and คอยาว and ตัวสีเหลืองลายสีน้ำตาล and กินพืช Then ยีราฟ',
    'if สัตว์เลี้ยงลูกด้วยน้ำนม and ตัวอ้วน and สีชมพู and มีเสียงร้อง อู๊ดๆ Then หมู',
    'if สัตว์เลี้ยงลูกด้วยน้ำนม and ตัวสีเหลืองสลับดำ and ดุร้าย and ว่องไว Then เสือ',
    'if สัตว์เลี้ยงลูกด้วยน้ำนม and ตัวเล็ก and หางยาว and ชอบแทะ Then หนู',
    'if สัตว์เลี้ยงลูกด้วยน้ำนม and ขนฟู and ขอบตาดำ and ชอบกินไผ่ Then หมีแพนด้า',
    'if สัตว์เลี้ยงลูกด้วยน้ำนม and มีเขา and กินพืช and ใช้ไถ่นา Then ควาย',
    'if สัตว์เลี้ยงลูกด้วยน้ำนม and มีนิสัยขี้เกียจ and มีเสียงร้อง เมี๊ยวๆ and ชอบนอน Then แมว',
    'if สัตว์เลี้ยงลูกด้วยน้ำนม and ส่งเสียงเห่า and แสนรู้ and มีสี่ขา Then สุนัข ',
    'if สัตว์เลี้ยงลูกด้วยน้ำนม and ตัวเป็นลายทาง and ตัวสีดำสลับขาว Then ม้าลาย',
    'if สัตว์เลี้ยงลูกด้วยน้ำนม and ล่าเหยื่อ and เจ้าป่า Then สิงโต',
    'if หายใจทั้งบนบกและในน้ำ and ออกลูกเป็นไข่ Then สัตว์ครึ่งบกครึ่งน้ำ',
    'if สัตว์ครึ่งบกครึ่งน้ำ and สีเขียว and กินแมลง Then กบ',
    'if สัตว์ครึ่งบกครึ่งน้ำ and ผิวขรุขระ and ชอบอยู่ที่ชื้น Then คางคก',
    'if ไม่มีขา and ลิ้นสองแฉก Then สัตว์เลื้อยคลาน', 
    'if สัตว์เลื้อยคลาน and ลำตัวยาว and กินเนื้อ and ลอกคราบได้ Then งู',
    'if หายใจในน้ำ and ออกลูกเป็นไข่ Then สัตว์น้ำ',
    'if สัตว์น้ำ and ตัวผู้ตั้งท้อง and มีครีบ Then ม้าน้ำ',
    'if สัตว์น้ำ and มีเหงือก and มีครีบ and ตากลม Then ปลา',
    'if สัตว์น้ำ and ลำตัวปล้อง and มีนวด Then กุ้ง',
    'if มีปีก and ออกลูกเป็นไข่ Then สัตว์ปีก', 
    'if สัตว์ปีก and มีหงอน and ส่งเสียงขัน Then ไก่',
    'if สัตว์ปีก and ปากแหลม and กินหนอน and บินได้ Then นก',
    'if สัตว์ปีก and อยู่ตามทะเล and ตัวสีขาว and หนีอากาศหนาว Then นกนางนวล',
    'if สัตว์ปีก and วิ่งไว and สีดำ and บินไม่ได้ Then นกกระจอกเทศ',

]

BlackBoard = []
StartingNode = []
TherminalNode = []

def rulelist():
    global kb_count
    kb_count = 1
    print("=========[ กฏทั้งหมด ]=========")
    for i in Knowledge:
        print(str(kb_count) + ") " + i)
        kb_count = kb_count + 1
    print("กฏที่มีทั้งหมด " + str(kb_count - 1))
    kb_count = 0

def startmenu(first):
    global respon
    respon = ""
    if first == True:

        print("")
        print("=================================================")
        print("ระบบ Expert System By CPE SWU ID: 165 491 492 508")
        print("=================================================")
        print("")

    # ระบบเพิ่ม กฏโดยผู้ใช้
    while True:
        try:
            print("คุณต้องการที่จะใช้ กฏที่มีอยู่แล้ว หรือ ต้องการเพิ่มกฏเอง")
            print("[พิมพ์ 0 เพื่อใช้กฏที่มีอยู่ตอนนี้ ] \n[พิมพ์ 1 เพื่อแก้ไข/ดูกฏ] ")
            respon = int(input(">> "))
            print("")


        except ValueError:
            print("กรุณาใส่เป็นตัวเลข")
            continue
        else:
            retun = respons(respon)
            if retun == 0:
                respons(1)
            break

def respons(respons):
    global submanu_1,num_premise
    if str(respons) == "1":
        while True:
            try:
                rulelist()
                print("")
                print("[พิมพ์ 0 เพื่อกลับไปหน้าแรก] \n[พิมพ์ 1 เพื่อเพิ่มกฏใหม่] \n[พิมพ์ 2 เพื่อลบกฏ] \n[พิมพ์ 3 เพื่อลบกฏทั้งหมด]")
                submanu_1 = int(input(">> "))
            except ValueError:

                continue
            else:
                if submanu_1 == 0:
                    startmenu(True)
                    break
                if submanu_1 == 1:
                    while True:
                        try:
                            print("")
                            print("กรุณาใส่จำนวนกฏที่ต้องการจะเพิ่ม")
                            num_rule = int(input(">> "))
                        except ValueError:
                            print("คุณใส่จำนวนผิด กรุณาใส่จำนวนเป็นตัวเลข")
                            continue
                        else:
                            for i in range(num_rule):
                                temp_rule = ""
                                print("กรุณาใส่จำนวน premise ของกฏข้อที่ " + str(i + 1))
                                while True:
                                    try:
                                        num_premise = int(input(">> "))
                                    except ValueError:
                                        print("คุณใส่จำนวนผิด กรุณาใส่จำนวนเป็นตัวเลข")
                                        continue
                                    else:
                                        break
                                for o in range(num_premise + 1):

                                    print("กฏข้อที่ " + str(i + 1) + " premise ที่ " + str(o + 1))
                                    if str(o) == "0":
                                        pre = input("if ")
                                        pre = "if " + pre
                                        temp_rule = temp_rule + pre
                                    elif str(o) == str(num_premise):
                                        pre = input(temp_rule + " Then ")
                                        pre = " Then " + pre
                                        temp_rule = temp_rule + pre
                                    else:
                                        pre = input(temp_rule + " and ")
                                        pre = " and " + pre
                                        temp_rule = temp_rule + pre
                                Knowledge.append(temp_rule)
                                print("")
                                print("[Status] \nทำการเพิ่มกฏ \"" + temp_rule + "\" สำเร็จ !")
                                print("")

                            startmenu(False)
                            break
                if submanu_1 == 2:
                    print("กรุณาใส่เลขกฏที่ต้องการจะลบ (1-"+str(len(Knowledge))+")")
                    while True:
                        try:
                            del_num = int(input(">> "))
                        except ValueError:
                            print("กรุณาใส่เป็นจำนวนตัวเลข !")
                            continue
                        else:
                            if int(del_num) <= int(len(Knowledge)):
                                Knowledge.pop(del_num-1)

                                return 0

                            break
                if submanu_1 == 3:
                    print("ท่านแน่ใจว่าจะลบกฏทั้งหมดหรือไม่ (Y = Yes, N = No)")
                    qus = input(">> ")
                    if qus.upper() == "Y":
                        Knowledge.clear()
                        return 0
                    else:
                        return 0

                break

    if respons == 0:
        return

startmenu(True)
# แปลง if and then เป็น code
for kn in Knowledge:
    # kn = kn.lower()
    if "if" or "and" or "Then" in kn:
        kn = kn.replace("if", "")
        kn = kn.replace("and", "")
        kn = kn.replace("Then", "")
    newkn = kn.split()
    KB.append(newkn)

# Get fact From user

print("กรุณาใส่รายละเอียดที่คุณเจอ (Problem Fact) ")
print("ตัวอย่าง: กินแมลง ส่งเสียงร้องในลำคอ")
BlackBoard = [str(BlackBoard) for BlackBoard in input(">> ").split()]

if BlackBoard != "":  # ถ้าผู้ใช้ป้อนข้อมูล
    input_fact = False
'''if input_fact_txt != "":  # ถ้าผู้ใช้ป้อนข้อมูล
    inputdata = input_fact_txt.split()
    for data in inputdata:
        BlackBoard.append(data)
else:  # ถ้าผู้ใช้ไม่ป้อนข้อมูล
    input_fact = False
'''
# เก็บ TherminalNode ไว้ในตัวแปร ปล.ยังไม่ได้แยกเอา intermidiant Node ออก
for ther in KB:
    TherminalNode.append(str(ther[len(ther) - 1]))
    ThenPart.append(ther[len(ther) - 1])
# เก็บ Starting Node ไว้ในตัวแปร
# Starting node คือ ตัวที่ไม่อยู่ใน then

for a in KB:  # นำข้อมูล array ตัวแรก ของ array ใน KB มาเก็บไว้ใน a
    # ข้อมูลที่ได้คือ a มีค่า ['orange','circle','orange']
    len_a = len(a)
    check = 0
    while check < len_a - 1:
        for b in KB:  # นำข้อมูล array ตัวแรก ของ array ใน KB มาเก็บไว้ใน b

            if (str(a[check]) == str(b[len(b) - 1])):  # ถ้า a ตัวที่ check ตรงกับ b ใน then part
                inThen = inThen + 1  # เพิ่มค่าตัวแปร inThen ให้เพิ่มขึ้น 1
                if (str(a[check]) in TherminalNode):
                    TherminalNode.remove(a[check])  # ลบตัวที่เป็น intermidiant node ออกจาก therminalnode

        if inThen == 0:  # ถ้าไม่ตรงกับใน then เลย
            StartingNode.append(a[check])  # เพิ่ม a ตัวที่ check ใน starting node
        inThen = 0  # reset ค่าใหม่ แล้วก็ลูปเช็คไปเรื่อยๆ
        check = check + 1  # เช็คตัวถัดไป

StartingNode = list(set(StartingNode))  # ลบตัวซ้ำ

def premiseRemain(numpr):
    pr2 = numpr

    if (int(lengthRule) - int(pr2)) == 0:
        status = False
    else:
        status = True
    return status

ansNot = []
numPremise = 0
notin = []
ansYes = []
skiprule = False
# main LOOP
for rule in KB:

    lengthRule = len(rule) - 1

    numPremise = 0
    for premise in rule[0:lengthRule]:
      if premise not in ansNot:
        numPremise = numPremise + 1
        if premise in BlackBoard:
            premiseinBB = True
            if premiseRemain(numPremise) == False:
                for p1 in rule:
                    if p1 not in BlackBoard:
                        BlackBoard.append(p1)
        else:
            if premise in StartingNode:
                print(str(premise) + " ? (y = yes, n = No)")
                response = input()
                if str(response.upper()) == "Y":
                    if premiseRemain(numPremise) == False:
                        for p2 in rule:
                            if p2 not in BlackBoard:
                                BlackBoard.append(p2)
                else:
                  ansNot.append(premise)
                  break
            else:

                break
      else:
        break

for th in TherminalNode:
    for bbb in BlackBoard:
        if str(th) == str(bbb):
            Concluding.append(th)
concludTxt = ""
Concluding = list(set(Concluding))  # ลบตัวซ้ำ
count = 0
print(" ")
print(" ")
if Concluding != []:
    if len(Concluding) > 1:
        for con in Concluding:
            if count < len(Concluding) - 1:
                concludTxt = concludTxt + con + " และ "
                count = count + 1
            else:

                concludTxt = concludTxt + con + ""
    else:
        for con in Concluding:
            concludTxt = concludTxt + con + ""
    print("มันคือ " + str(concludTxt))
else:
    print("ไม่มีคำตอบ (ปัญหานี้ใช้ไม่ได้กับ KB นี้)")

# BlackBoard = list(set(BlackBoard)) # ลบตัวซ้ำ
print(" ")

print(" ")
# Rule Teacher

# Debug
if debug == True:
    print("--------------- > DEBUG Enable <-------------- ")
    print("BlackBoard = " + str(BlackBoard))
    print("StartingNode = " + str(StartingNode))
    print("TerminalNode = " + str(TherminalNode))
    print("ThenPart = " + str(ThenPart))





