print('import_test0 start')
print('__name__ = {}'.format(__name__))

def main():
    print('main executed')

# このファイルが、
# 呼び出す側 → __name__ == __main__ → main関数が実行される
# 呼び出される側 → __name__ == import_test0でmain()は実行されない
if __name__ == '__main__':
    main()