def compress_text(text):

    compressedText = ''
    count = 1

    #print("Length of text is: " + str(len(text)))

    for index in range(1, len(text)):
        #1, 2
        #compare current character to previous character, if they are same then add 1 to count
        if text[index] == text[index - 1]:
            count += 1
        #if current and previous character are not the same, then get the previous character (index - 1) and append the count for that character
        else:
            compressedText += text[index - 1] + str(count)
            count = 1
    
    compressedText += text[-1] + str(count)

    return compressedText        


print(compress_text("abbc"))
#print(compress_text("aaaaabcddddddd"))