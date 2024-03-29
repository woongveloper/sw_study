# Contents
0. Method 란
1. Method (sequence - str)
2. Method (sequence - list)
3. Method (Non_sequence - set)
4. Method (Non_sequence - dict)

## Method
- 객체에 속한 함수로 객체의 상태를 조작하거나 동작을 수행한다.
- class 내부에 정의되는 함수
- `데이터 타입 객체`.`method()`로 호출

### 1. Method - str
---

📌***찾기, 위치 반환 method***
|        메서드      	|                                         설명                                        	|
|:------------------:	|:-----------------------------------------------------------------------------------:	|
|      s.find(x)     	|     x의   첫 번째 위치를 반환. 없으면,   -1을 반환                                  	|
|      s.index(x)    	|     x의   첫 번째 위치를 반환. 없으면,   오류 발생                                  	|
|     s.isalpha()    	|     알파벳 문자 여부      *단순 알파벳이 아닌 유니코드 상 Letter (한국어도 포함)    	|
|     s.isupper()    	|     모두 대문자야?                                                                     	|
|     s.islower()    	|     모두 소문자야?                                                                	|
|     s.istitle()    	|     타이틀   형식 여부                                                              	|
|     isdecimal()  	|  문자열이 모두 숫자로만 이루어져 있어?                                                                        	|
|     isdigit()  	|   문자열이 모두 숫자로만 이루어져 있어? (유니코드 숫자들도 포함)                                                                  	|
|     isnumeric()  	|  문자열이 모두 수로 이루어져 있어? (분수, 지수, 루트 등 모두 포함)                                                                	|

📌***문자열을 수정하는 method***
|                  메서드                 	|                                              설명                                            	|
|:---------------------------------------:	|:--------------------------------------------------------------------------------------------:	|
|       s.replace(old,   new[,count])     	|     바꿀 대상 글자를 새로운 글자로 바꿔서 반환                                               	|
|             s.strip([chars])            	|     공백이나 특정 문자를 제거                                                                	|
|     s.split(sep=None,   maxsplit=-1)    	|     공백이나 특정 문자를 기준으로 분리                                                       	|
|       'separator'.join([iterable])      	|     구분자로 iterable을   합침('-'.join(words) 꼴)                                                               	|
|              s.capitalize()             	|     가장   첫 번째   글자를   대문자로   변경                                                	|
|                 s.title()               	|     문자열 내 띄어쓰기 기준으로 각 단어의 첫 글자는 대문자로,      나머지는 소문자로 변환    	|
|                 s.upper()               	|     모두   대문자로 변경                                                                     	|
|                 s.lower()               	|     모두   소문자로 변경                                                                     	|
|               s.swapcase()              	|     대↔소문자 서로 변경                                                                      	|

📌***문자열에 포함된 유형 판별***

### 2. Method - list
---
📌***list 연장, 삽입***
|          메서드         	|                                                   설명                                                  	|
|:-----------------------:	|:-------------------------------------------------------------------------------------------------------:	|
|        L.append(x)      	|     리스트   마지막에 항목 x를   추가                                                                   	|
|        L.extend(m)      	|     Iterable m의   모든 항목들을 리스트 끝에 추가 (+=과   같은 기능)                                    	|
|     L.insert(i,   x)    	|     리스트   인덱스 i에 항목 x를 삽입                                                                   	|


📌***list 삭제***

|          메서드         	|                                                   설명                                                  	|
|:-----------------------:	|:-------------------------------------------------------------------------------------------------------:	|
|        L.remove(x)      	|     리스트   가장 왼쪽에 있는 항목(첫 번째)   x를   제거     항목이 존재하지 않을 경우,   ValueError    	|
|          L.pop()        	|     리스트   가장 오른쪽에 있는 항목(마지막)을   반환 후 제거                                           	|
|         L.pop(i)        	|     리스트의 인덱스 i에   있는 항목을 반환 후 제거                                                      	|
|         L.clear()       	|     리스트의 모든 항목 삭제                                                        
                     	

📌***list 정렬, index 및 개수 반환***
|               문법              	|                                   설명                                 	|
|:-------------------------------:	|:----------------------------------------------------------------------:	|
|     L.index(x,   start, end)    	|     리스트에   있는 항목 중 가장 왼쪽에 있는 항목 x의 인덱스를 반환    	|
|            L.reverse()          	|     리스트의 순서를 역순으로 변경 (정렬 X)|
|             L.sort()            	|     리스트를 정렬 (매개변수   이용가능)                                	|
|            L.count(x)           	|     리스트에서 항목   x의 개수를 반환                                  	|

### 3. Method - set
---
📌***set 항목 추가/제거***
|           메서드          	|                                설명                               	|
|:-------------------------:	|:-----------------------------------------------------------------:	|
|          s.add(x)         	|     세트 s에 항목   x를 추가. 이미   x가 있다면 변화 없음         	|
|          s.clear()        	|     세트 s의   모든 항목을   제거                                 	|
|         s.remove(x)       	|     세트 s에서   항목 x를 제거. 항목   x가 없을 경우 Key error    	|
|           s.pop()         	|     세트 s에서   랜덤하게 항목을 반환하고,   해당 항목을 제거     	|
|        s.discard(x)       	|     세트 s에서   항목 x를 제거                                    	|
|     s.update(iterable)    	|     세트 s에   다른 iterable 요소를   추가                        	|

📌***set의 집합 성질***
|              메서드            	|                                         설명                                       	|         연산자        	|
|:------------------------------:	|:----------------------------------------------------------------------------------:	|:---------------------:	|
|      set1.difference(set2)     	|차집합|      set1   – set2    	|
|     set1.intersection(set2)    	|교집합|     set1   & set 2    	|
|       set1.issubset(set2)      	|set2에 set1이 속해있냐|     set1   <= set2    	|
|      set1.issuperset(set2)     	|set1에 set2가 속해있냐|     set1   >= set2    	|
|         set1.union(set2)       	|합집합|     set1   \| set2    	|

### 4. Method - dictionary
📌***제거***
|            메서드           	|                                                                                설명                                                                              	|
|:---------------------------:	|:----------------------------------------------------------------------------------------------------------------------------------------------------------------:	|
|           D.clear()         	|     딕셔너리 D의   모든 키/값 쌍을 제거                                                                                                                          	|
|           D.get(k)          	|     키 k에   연결된 값을 반환 (키가 없으면 None을 반환)                                                                                                          	|
|         D.get(k,   v)       	|     키 k에   연결된 값을 반환하거나 키가 없으면 기본 값으로 v를 반환                                                                                             	|
|           D.keys()          	|     딕셔너리 D의   키를 모은 객체를 반환                                                                                                                         	|
|          D.values()         	|     딕셔너리 D의   값을 모은 객체를 반환                                                                                                                         	|
|           D.items()         	|     딕셔너리 D의   키/값 쌍을 모은 객체를 반환(tuple들로 이루어진 list)                                                                                                                   	|
|           D.pop(k)          	|     딕셔너리 D에서   키 k를 제거하고 연결됐던 값을 반환 (없으면   오류)                                                                                          	|
|         D.pop(k,   v)       	|     딕셔너리 D에서   키 k를 제거하고 연결됐던 값을 반환 (없으면   v를 반환)                                                                                      	|
|        D.setdefault(k)      	|     딕셔너리 D에서   키 k와 연결된 값을 반환                                                                                                                     	|
|     D.setdefault(k,   v)    	|     딕셔너리 D에서   키 k와 연결된 값을 반환한다. D에 존재하지 않는 key, value라면 이를 딕셔너리에 추가한다.                                 	|
|        D.update(other)      	|     other 내 각 키에 대해 D에   있는 키면 D에 있는 그 키의 값을 other에 있는 값으로 대체.     other에 있는 각 키에 대해 D에   없는 키면 키/값 쌍을 D에   추가    	|

