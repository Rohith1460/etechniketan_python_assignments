# Assignment 2 Answers

# MCQ Answers
# 1. d
# 2. b
# 3. b
# 4. b
# 5. c
# 6. b
# 7. b
# 8. a
# 9. c
# 10. b
# 11. b
# 12. d
# 13. d
# 14. d
# 15. b
# 16. d
# 17. d
# 18. d
# 19. b
# 20. c
# 21. c
# 22. a
# 23. d
# 24. c
# 25. d
# 26. b
# 27. d
# 28. a
# 29. d
# 30. b
# 31. d
# 32. d


# Q33
s1 = 'practice is important to perfectly learn python'
indexes = []
for i in range(len(s1)):
    if s1[i] == 'p':
        indexes.append(i)
print(indexes)


# Q34
strings = ["aba", "ab", "racecar", "hi", "1991", "level", "no", "civic"]
count = 0
for s in strings:
    if len(s) > 2:
        if s == s[::-1]:
            count += 1
print(count)


# Q35
s1 = 'How much wood would a woodchuck chuck if a Woodcutter could chuck wood to build a wooden house to woo his wife'
words = s1.split()
result = []
for w in words:
    if len(w) >= 4 and (w[0] == 'w' or w[0] == 'W'):
        if w not in result:
            result.append(w)
print(result)
