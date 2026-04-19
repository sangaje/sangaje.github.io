+++
title = "BST-AVL Tree (1) 기초"
author = ["Bomin Lee"]
tags = ["자료구조"]
categories = ["자료구조"]
draft = true
+++

## AVL Tree란? {#avl-tree란}

AVL Tree는 자가 균형 이진 탐색 트리 (self-balancing BST)의 한 종류로, 1962년 G. M. Adel'son-Vel'skii 과 E. M. Landis의 논문에서 처음 소개되었으며<a href="#citeproc_bib_item_1">[1]</a>, AVL Tree의 이름 AVL 은 이 두 사람의 이름에서 따온 것이다. 이는 각 노드의 왼쪽과 오른쪽 서브트리의 높이 차이가 최대 1이 되도록 유지하는 트리 구조로, 삽입과 삭제 연산 후에도 균형을 유지하기 위해 회전 연산을 사용한다. AVL Tree는 균형 조건을 엄격하게 유지하기 때문에 삽입과 탐색 연산이 빠르다. 하지만 해당 연산 시 추가적인 회전 연산이 필요하므로, 구현이 기존의 BST에 비해 다소 복잡하다.

기존의 BST에서는 삽입과 삭제 연산이 트리의 균형을 깨뜨릴 수 있지만, AVL Tree에서는 이러한 연산 후에도 균형을 유지하기 위해 회전 연산이 수행된다. 예를 들어, 노드가 삽입된 후에 균형이 깨진 경우, 단일 회전 또는 이중 회전을 통해 트리를 재구성하여 균형을 회복한다. 이러한 회전은 트리의 높이를 최소화하여 탐색 속도를 유지하는 데 중요한 역할을 한다.


## AVL Tree의 균형 계수 {#avl-tree의-균형-계수}

AVL Tree는 각 노드에 균형 계수 (balance factor)를 저장하여, 각 노드의 왼쪽과 오른쪽 서브트리의 높이 차이를 나타낸다. 균형 계수는 -1, 0, 1 중 하나의 값을 가지며, 이 값이 범위를 벗어날 경우 트리가 불균형하다고 판단한다. 삽입이나 삭제 연산 후에 균형 계수가 범위를 벗어나면, 트리를 재구성하여 균형을 회복한다. [1](#figure--fig:avl-cases)은 AVL Tree에서 발생할 수 있는 4가지 불균형 케이스 (LL, RR, LR, RL)를 보여주며 이때 균형 계수 \\(BF\\) 는 아래의 식과 같의 정의된다. 그림에서 최 상단 노드의 균형 계수는 +2 또난 -2로, \\({-1,0,+1}\\) 에 속해있지 않아 불균형하다고 할 수 있다. 사실 그림만 봐도 한쪽으로 쏠려있는 것을 알 수 있지만, 컴퓨터로 연산할 때마다 사람의 눈으로 확인할 수는 없으므로, 균형 계수를 계산하여 불균형 여부를 판단하는 것이다.
\\[BF=h(v\_{left})-h(v\_{right})\\]
\\[example-LL case: BF\_{top}=h(v\_{left})-h(v\_{right})=2-1=0\\]

<a id="figure--fig:avl-cases"></a>

{{< figure src="/ox-hugo/avl_all_cases_bordered.png" caption="<span class=\"figure-number\">Figure 1: </span>AVL 트리의 4가지 불균형 케이스 (LL, RR, LR, RL)" >}}

## References

<div class="csl-bib-body">
  <div class="csl-entry"><a id="citeproc_bib_item_1"></a>
    <div class="csl-left-margin">[1]</div><div class="csl-right-inline">G. Adelson-Velsky and E. M. Landis, “An algorithm for the organization of information,” <i>Soviet mathematics doklady</i>, vol. 3, pp. 1259–1263, 1962, <a href="https://zhjwpku.com/assets/pdf/AED2-10-avl-paper.pdf">https://zhjwpku.com/assets/pdf/AED2-10-avl-paper.pdf</a></div>
  </div>
</div>
