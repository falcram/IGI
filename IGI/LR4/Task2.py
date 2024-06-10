import re
import zipfile
# регулярка для пароля (?=.*[0-9])(?=.*[A-Z])(?=.*[a-z])([A-Z0-9a-z_]){8,}
# ((?<=[^\.])(\.\s)|!\s|\?\s|!!!\s|(\...)\s) до (\. |! |\? |!!! )
def Task2():
    def count_sentences(inp_text):
        res = re.findall(r"((?<=[^\.])(\.\s)|!\s|\?\s|!!!\s|(\...)\s)", inp_text)
        #print(res)
        return len(res)
    def every_type_of_sent(inp_text):
        amount_narrative = re.findall(r"((?<=[^\.])(\.(\s|$))|(\.\.\.)(\s|$))", inp_text)
        amount_interrogative = re.findall(r"\?\s", inp_text)
        amount_incentive = re.findall(r"(?<=[^!])!\s|!!!\s", inp_text)
        return len(amount_narrative), len(amount_interrogative), len(amount_incentive)
    def average_word_length(inp_text):
        #word_list = re.findall(r"(?<=\s|\(|\)|\"|'|\.|,|;|:)[a-zA-Z'0-9]+(?=\s|\(|\)|\"|'|\.|,|;|:)", inp_text)
        word_list = re.findall(r"\b[a-zA-Z'0-9]+\b", inp_text)
        sum = 0
        for w in word_list:
            sum += len(w)
        return sum/len(word_list)
    def average_sentence_length(inp_text):
        sentence_list = re.findall(r"[\w ,:;()\"']+", inp_text)
        sum = 0
        for s in sentence_list:
            word_list = re.findall(r"\b[a-zA-Z'0-9]+\b", s)
            for w in word_list:
                sum+=len(w)
        return sum/len(sentence_list)
    def print_words_A_0(inp_text):
        res = re.findall(r"\b(?=.*[A-Z])(?=.*[0-9])([A-Z0-9]+)\b", inp_text)
        output_str = "Words that contains only upper case letters and decimals: "
        for i in res:
            print(i[1])
            output_str += i[1]
            output_str += ", "
        return output_str
    def count_A_Z_words(inp_text):
        return len(re.findall(r"\b([A-Z]+)\b", inp_text))
    def find_longest_l_word(inp_text):
        l_words = re.findall(r"\bl[A-Za-z]+\b",inp_text)
        w_length = 0
        res = ""
        for i in l_words:
            if(len(i)>w_length):
                w_length = len(i)
                res = i
        return res
    def print_repeat_words(inp_text):
        words_list = re.findall(r"\b[A-Za-z0-9']+\b",inp_text)
        res = set()
        for w in range(len(words_list)-1):
            i = w+1
            if(i > len(words_list)-1):
                break
            while(i!=len(words_list)-1):
                if words_list[w]== words_list[i]:
                    res.add(words_list[w].lower())
                    break
                i+=1
        output = "Words that repeats in the text: "
        for r in res:
            output += r + ", "
        output += "\n"
        return output    
        
         

    def check_smile(inp_text):
        res = re.findall(r"(;|:)(-*)((\()|(\))|(\[)|(\]))+", inp_text)#^(;|:)-*(\(|\)|\[|\])+$
        check = 0
        for i in res:
            for j in range(3,7):
                if i[j] !='':
                    check+=1
        if(check == 1):
            #print("It is smile")
            return "It is a smile"
        else:
            return "It is NOT a smile"
            #print("It is NOT smile")           

    def check_password(inp_password):
        res = re.match(r"(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z])^([A-Z0-9a-z_]){8,}$", inp_password)
        if res != None:
            #print("Strong Password")
            #return True
            return "Strong Password"
        else:
            #print("Weak Password")
            #return False
            return "Weak Password"

    text = " "
    with open("text.txt", "r") as file:
        text += file.read() 
    text = text+" " 
    answer = ""    
    answer += print_words_A_0(text)+ "\n"
    answer += "Amount of sentences: "
    answer += str(count_sentences(text)) + "\n"
    amount_narrative_1, amount_interrogative_1, amount_incentive_1 = every_type_of_sent(text)
    answer += f"Amount of narrative: {amount_narrative_1}\nAmount of interrogative: {amount_interrogative_1}\nAmount of incentive: {amount_incentive_1}\n"
    answer += "Average word length: " + str(average_word_length(text)) + "\n"
    answer += "Average sentence length: " + str(average_sentence_length(text)) + "\n"
    answer += "Amount of words that contains only upper case letters: " + str(count_A_Z_words(text)) + "\n"
    answer += "Longest word that starts with \"l\": " + find_longest_l_word(text) + "\n"
    answer += print_repeat_words(text)
    print("\nWrite your smile:")
    #smile = input()
    smile = ":-)"
    answer += smile + " : " + check_smile(smile) + "\n"
    print("\nWrite your password:")
    #password = input()
    password = "A0asdasd1_ad03"
    answer += password + " : " + check_password(password) + "\n"
    print(answer)

    file = open('Result.txt', 'w')
    file.write(answer)
    file.close()
    zip_path = "TASK2_RESULT.zip"
    file_path = 'Result.txt'
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        zipf.write(file_path, arcname='Result.txt')    
#Task2()