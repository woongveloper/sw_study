![image](https://github.com/woongveloper/sw_study/assets/156386797/1f7a8d51-2367-428f-a193-0f46a748d6d8)
<img src="https://github.com/woongveloper/sw_study/assets/156386797/e9434839-78a5-4acb-8ceb-2cc16582bff1.png" width="250" height="400"/>
# python을 잊지 않기 위해
- 갑자기 든 생각인데, 다른 공부한다고 python을 잊어버리는건 아닌가 생각을 하게 되었음. 그래서 시작한 dontForgetPython
  - 실제로 많이 까먹었음.
- 주 1,2회 알고리즘 문제 풀이 진행.
- 당장 어려운 것을 풀 필요는 없다. 이미 A형은 취득했으니, 감각을 올리는 것을 목표로 부담이 되지 않는 선에서 진행한다. (백준 실버 6월, 이후 골드1 복귀)

## 24.06 알고리즘 일기
- 24.06.12: 백준 실버4 - 설탕배달 : DP, dfs 활용해서 해봤음.
- 24.06.12: 백준 실버3 - 터렛 : 두개의 원, 접점의 개수 문제. 굉장히 오래걸렸음. r1,r2와 중심간의 거리 이 세가지의 관계 다시 생각해보기.
- 24.06.23: 백준 실버4 - 큐 : sys.stdin.readline.rstrip('\n')
- 24.06.26: 백준 실버2 - DFS/BFS : DFS에서 Stack 추가하는것에 오류가 났음. 오류의 내용은 다음과 같음.
  - 다 잘짯는데 하나가 문제였음. 그것은! 바로 stack에 push할 때 target이 아닌 현 위치를 추가하는 것임
  - 이게 무슨소리냐! 하면, 만약 1번 노드에서 2번노드로 가는 상황을 보자? 그 상황에서 stack에는 현 위치인 1이 추가되어야함. 2가 추가되면 안된단 말!
- 24.06.26: 백준 실버2 - 배추배추양배추 : 2차원 배열, delta사용, 위에보다 오히려 쉬웠다. DFS를 삽질한거같은데, DFS 숙달 필요

## 24.07
- 24.07.01: 백준 실버1 - 미로찾기 : bfs + 숫자 적으면서 진행
- 24.07.01: 백준 실버1 - RGB거리 : DP를 사용했어야 한다. 처음엔 DFS/백트레킹을 시도, 하지만 3**N이라는 시간복잡도로 시간초과 발생.
  - DP문제에 취약한것 같음.
  - DP를 풀때, 이것을 뽑으려면 전에 어떤것을 뽑아야할까? 와 같은 앞서서 바라보는? 자세가 필요한 것 같다.
- 24.07.05: 백준 실버1 - 단지 : 무난한 bfs