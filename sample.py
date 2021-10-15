math = 89
science = 76
chemistry = 75
english = 98

total = math + science + chemistry + english
average = total / 4
print(average)

subject = (89, 76, 75, 98)
# subject[0] = 100
total1 = subject[0] + subject[1] + subject[2] + subject[3]
average1 = total1 / 4
print(average1)

subject2 = [89, 76, 75, 98]
subject2[0] = 100
total2 = subject2[0] + subject2[1] + subject2[2] + subject2[3]
average2 = total2 / 4
print(average2)




# リストについて
weekdays = ['Monday' ,'Tuesday', ' Wednesday', 'Thursday', 'Friday', 'Saturday']
weekdays.append('Sunday')
print(weekdays)

animals = ['cat', 'dog', 'lion', 'mouse', 'roba']
animals.insert(1, 'elephant')
print(animals)
# del animals[1]
animals.pop(1)
print(animals)




# リストについて
#　ゲームでは位置情報（ｘ座標、y座標の値）を頻繁扱うが、そのときにリストが使われる
weekdays2 = ('Monday' ,'Tuesday', ' Wednesday', 'Thursday', 'Friday', 'Saturday')
# weekdays2.append('Sunday') #エラーが出る

pos = (12, 76)
print(pos)
print(pos[0])
# x, y座標をそれぞれ別の変数に代入したいときはこうする
pos_x, pos_y = pos
print(pos_x)
print(pos_y)
# これをアンパックと呼ぶ

#これを応用すると座標を入れ替えることが出来る
x = 3
y = 6
(x, y) = (y, x)
print('x:{}'.format(x))
print('y:{}'.format(y))



# 辞書
score = {
    'math': 76,
    'science': 98, 
    'chemistry': 76,
    'english': 45
}
print(score)
print(score['english'])
print(score['math'])




# リストのリスト、タプルのリストなど応用編
#タプルの中にタプルを入れたデータ構造
animals = ('Horse', 'Rabbit', 'Dog')
scores = (23,54,67)
data = (animals, scores)
print(data)
#要素へのアクセスは今までどおり
print('data[0]:{}'.format(data[0]))
#更に深く要素へアクセス
print('data[0][2]:{}'.format(data[0][2]))



#マルバツゲームを作る際に必要なデータ構造
#hint: リストのリストを使う
data = [[0,0,1],[ 1,2,2],[0,0,0]]
print(data)
data[0][1] = 1
print(data)
data[2][1] = 1 
print(data)






# リストやタプルを扱うのに便利な関数

# len
print(len([1,2,3]))
print(len([[1,2,3], [4,5,6], [7,8,9,10]]))
datas = [[1,2,3], [4,5,6], [7,8,9,10]]
print(len(datas[2]))



# copy
a = [1,2,3]
b = a
a[0] = 0
print(a)
print(b)
# どちらも[0,2,3]となる
# これは最初にリストを作成したときに、aは参照しているだけでリストそのものを格納していない
# 当然、bもリストを参照しているだけなのであるため、a,b両方とも同じ値を出力した結果となった

# 意図的にリストを複製したいときはcopyメソッドを使う
b  = a.copy()
a[0] = 9
print(a)
print(b)
# 異なる結果が出力された
# この結果から言えるのは、a,bはそれぞれ別のリストを参照しているということ


# in ある要素がリストやタプルに含まれているかチェックするときに使用する
greets = ('morning', 'afternoon', 'evening')
print('noon' in greets)
print('morning' in greets)
# .index 要素が何番目の格納されているか確認する場合に使用する
print('afternoon is {}番目'.format(greets.index('afternoon') + 1))



# リストを並び替える方法
# sorted関数、 sortメソッド
fruits = ['banana', 'apple', 'orange', 'grape']
print(sorted(fruits))
fruits.sort()
print(fruits)



# print
print('1=%s 2=%s' % ('hello', 'gooodbye'))
print('value=(%d, %d)' % (3,4))
# 後ろにタプル形式で書く




# 条件式
# if文
a = 4
if a:
    print('a is not zero')
else:
    print('a is zero')

print(bool(a))
print(bool(0))

# while文
counter = 0
while counter < 3:
    print(counter)
    counter += 1



# 各教科の平均点を求める

total = 0
index = 0
subject = (23,65,78,45)
while index < len(subject):
    total += subject[index]
    index += 1
average = total / len(subject)
print('average:{}'.format(average))


total = 0
for score in subject: #要素が一つずつ格納される
    total += score
average = total / len(subject)
print('average:{}'.format(average))


for letter in 'hello!':
    print(letter)



# 自由に数字を取得したいときはrange()関数
for index in range(5):
    print(index)

total = 0
for val in range(10):
    total += val
print(total)


for val in range(2,6):
    print(val)


# 一つ飛ばしで数字を取得したいとき
for val in range(1, 10, 2):
    print(val)

for val in range(2 ,11, 2):
    print(val)






# ループ処理に使える処理 while, break
count = 0
while True:
    if count > 3:
        break
    print(count)
    count += 1


for val in range(5):
    print(val)
    if val % 2 == 0:
        continue
    print("↑odd")