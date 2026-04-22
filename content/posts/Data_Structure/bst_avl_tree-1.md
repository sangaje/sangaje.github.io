+++
title = "BST-AVL Tree (1) 기초"
author = ["bomin"]
tags = ["자료구조"]
categories = ["자료구조"]
draft = false
+++

## <span class="org-todo todo TODO">TODO</span>  {#d41d8c}

> 이번 글은 AVL Tree에 대한 기초적인 개념과 회전 연산에 대해 설명한다. AVL Tree는 자가 균형 이진 탐색 트리의 한 종류로, 각 노드의 왼쪽과 오른쪽 서브트리의 높이 차이가 최대 1이 되도록 유지하는 트리 구조이다. 삽입과 삭제 연산 후에도 균형을 유지하기 위해 회전 연산을 사용한다. AVL Tree는 균형 조건을 엄격하게 유지하기 때문에 삽입과 탐색 연산이 빠르지만, 구현이 기존의 BST에 비해 다소 복잡하다.


## <span class="org-todo done DONE">DONE</span> AVL Tree란? {#avl-tree란}

AVL Tree는 자가 균형 이진 탐색 트리 (self-balancing BST)의 한 종류로, 1962년 G. M. Adel'son-Vel'skii 과 E. M. Landis의 논문에서 처음 소개되었으며<a href="#citeproc_bib_item_1">[1]</a>, AVL Tree의 이름 AVL 은 이 두 사람의 이름에서 따온 것이다. 이는 각 노드의 왼쪽과 오른쪽 서브트리의 높이 차이가 최대 1이 되도록 유지하는 트리 구조로, 삽입과 삭제 연산 후에도 균형을 유지하기 위해 회전 연산을 사용한다. AVL Tree는 균형 조건을 엄격하게 유지하기 때문에 삽입과 탐색 연산이 빠르다. 하지만 해당 연산 시 추가적인 회전 연산이 필요하므로, 구현이 기존의 BST에 비해 다소 복잡하다.

기존의 BST에서는 삽입과 삭제 연산이 트리의 균형을 깨뜨릴 수 있지만, AVL Tree에서는 이러한 연산 후에도 균형을 유지하기 위해 회전 연산이 수행된다. 예를 들어, 노드가 삽입된 후에 균형이 깨진 경우, 단일 회전 또는 이중 회전을 통해 트리를 재구성하여 균형을 회복한다. 이러한 회전은 트리의 높이를 최소화하여 탐색 속도를 유지하는 데 중요한 역할을 한다.


## <span class="org-todo done DONE">DONE</span> AVL Tree의 균형 계수 {#avl-tree의-균형-계수}

\\[
BF(v) := h(v\_{\text{left}}) - h(v\_{\text{right}})
\\]
\\[
S(n) := \begin{cases}
0 & \text{if } BF(n) = 0 \quad \text{(Perfect Equilibrium)} \\\\
1 & \text{if } BF(n) = 1 \quad \text{(Left-Skewed, Stable)} \\\\
-1 & \text{if } BF(n) = -1 \quad \text{(Right-Skewed, Stable)} \\\\
\text{Critical} & \text{if } |BF(n)| > 1 \quad \text{(Imbalanced)}
\end{cases}
\\]
\\[
example\_{\text{LL case}} : BF(v) = h(v\_{left})-h(v\_{right})= 2 - 0 = +2
\\]

AVL Tree는 각 노드에 균형 계수 (balance factor)를 저장하여, 각 노드의 왼쪽과 오른쪽 서브트리의 높이 차이를 나타낸다. 균형 계수는 -1, 0, 1 중 하나의 값을 가지며, 이 값이 범위를 벗어날 경우 트리가 불균형하다고 판단한다. 삽입이나 삭제 연산 후에 균형 계수가 범위를 벗어나면, 트리를 재구성하여 균형을 회복한다.그림[[1](#figure--fig:avl-cases)]은 AVL Tree에서 발생할 수 있는 4가지 불균형 케이스 (LL, RR, LR, RL)를 보여주며 이때 균형 계수 \\(BF\\) 는 위의 식과 같의 정의된다. 그림에서 최 상단 노드의 균형 계수는 +2 또난 -2로, \\({-1,0,+1}\\) 에 속해있지 않아 불균형하다고 할 수 있다. 사실 그림만 봐도 한쪽으로 쏠려있는 것을 알 수 있지만, 컴퓨터로 연산할 때마다 사람의 눈으로 확인할 수는 없으므로, 균형 계수를 계산하여 불균형 여부를 판단하는 것이다<a href="#citeproc_bib_item_2">[2]</a>.

<a id="figure--fig:avl-cases"></a>

{{< figure src="/ox-hugo/avl_all_cases_bordered.png" caption="<span class=\"figure-number\">Figure 1: </span>AVL 트리의 4가지 불균형 케이스 (LL, RR, LR, RL)" >}}


## <span class="org-todo done DONE">DONE</span> AVL Tree의 회전 연산 {#avl-tree의-회전-연산}

이전의 식과같이 AVL Tree의 균형 계수를 정했을때, 우리는 균형 계수의 절댓값이 1을 초과하면 이를 불균형 하다고 판단했다. 이는 AVL Tree는 \\(\forall v \in V\\)에 대해 그들 의 자식 노드 \\(v\_{left}, v\_{right}\\)의 높이 차이가 1 이상 차이나면 이를 다시 균형을 맞추는 과정이 필요함을 시사한다. AVL Tree는 이러한 균형을 맞추는 과정을 **회전** 을 통해 수행한다. 즉 앞서 본 그림[[1](#figure--fig:avl-cases)]에서 보이는 4가지 불균형 케이스 (LL, RR, LR, RL)에서 각각의 경우에 따라 알맞은 회전을 선택하여 수행해야 한다.


### LL Case (Left-Left) {#ll-case--left-left}

LL Case는 \\(HF(v)=2, HF(v\_{left})=1\\) 인 경우로, 그림[[2](#figure--fig:avl-ll-case)]와 같다. 그림과 같이 특정 노드에서의 자식 노드들의 높이 차이가 +2로 불균형 하며, 또한 그 좌측 자식 노드의 균현 계수가 +1인 경우이다. 즉, 특정 노드의 좌측, 그리고 그 노드의 좌측 자식 노드로 인해 불균형이 발생한 경우로 볼 수 있다.

<a id="figure--fig:avl-ll-case"></a>

{{< figure src="/ox-hugo/avl_ll_subtrees_rotation.png" caption="<span class=\"figure-number\">Figure 2: </span>AVL 트리의 LL 케이스에서의 불균형과 회전 과정" >}}

그림[[2](#figure--fig:avl-ll-case)]의 우측 크림은 LL 케이스에서의 불균형을 회전 연산을 통해 균형을 회복한 그래프이다. 좌측 그림의 빨간 **불균형이 발생한 노드** 는 좌측 노드에 의해 불균형이 발생으며 이를 **Right Rotation** 연산을 통해 균형을 회복했다. Right Rotation은 서브트리 내에서 불균형이 발생한 노드의 좌측 자식 노드를 새로운 루트로 만들고, 기존의 루트 노드는 새로운 루트의 우측 자식이 되는 회전 연산이다. 이 과정에서 트리의 높이 차이가 최소화되고 균형이 회복된다.


### RR Case (Right-Right) {#rr-case--right-right}

RR Case는 \\(HF(v)=-2, HF(v\_{right})=-1\\) 인 경우로, 그림[[3](#figure--fig:avl-rr-case)]와 같다. 그림과 같이 특정 노드에서의 자식 노드들의 높이 차이가 -2로 불균형 하며, 또한 그 우측 자식 노드의 균현 계수가 -1인 경우이다. 즉, 특정 노드의 우측, 그리고 그 노드의 우측 자식 노드로 인해 불균형이 발생한 경우로 볼 수 있다.

<a id="figure--fig:avl-rr-case"></a>

{{< figure src="/ox-hugo/avl_rr_subtrees_rotation.png" caption="<span class=\"figure-number\">Figure 3: </span>AVL 트리의 RR 케이스에서의 불균형과 회전 과정" >}}

그림[[3](#figure--fig:avl-rr-case)]의 우측 크림은 RR 케이스에서의 불균형을 회전 연산을 통해 균형을 회복한 그래프이다. 좌측 그림의 빨간 **불균형이 발생한 노드** 는 우측 노드에 의해 불균형이 발생하며 이를 **Left Rotation** 연산을 통해 균형을 회복했다. Left Rotation은 서브트리 내에서 불균형이 발생한 노드의 우측 자식 노드를 새로운 루트로 만들고, 기존의 루트 노드는 새로운 루트의 좌측 자식이 되는 회전 연산이다. 이 과정에서 트리의 높이 차이가 최소화되고 균형이 회복된다.


### LR Case (Left-Right) {#lr-case--left-right}

LR Case는 \\(HF(v)=2, HF(v\_{left})=-1\\) 인 경우로, 그림[[4](#figure--fig:avl-lr-case)]와 같다. 그림과 같이 특정 노드에서의 자식 노드들의 높이 차이가 +2로 불균형 하며, 또한 그 좌측 자식 노드의 균현 계수가 -1인 경우이다. 즉, 특정 노드의 좌측, 그리고 그 노드의 우측 자식 노드로 인해 불균형이 발생한 경우로 볼 수 있다.

<a id="figure--fig:avl-lr-case"></a>

{{< figure src="/ox-hugo/avl_lr_subtrees_rotation.png" caption="<span class=\"figure-number\">Figure 4: </span>AVL 트리의 LR 케이스에서의 불균형과 회전 과정" >}}

그림 [[4](#figure--fig:avl-lr-case)]의 좌측 크림은 LR 케이스에서의 불균형을 보여주는 그래프이다. 빨간 **불균형이 발생한 노드** 는 좌측 노드와 그 노드의 우측 자식 노드로 인해 불균형이 발생했다. LR 케이스는 단일 회전으로 해결되지 않으며, 두 단계의 회전이 필요하다. 첫 번째 단계에서는 불균형이 발생한 노드의 좌측 자식 노드에 대해 **Left Rotation** 을 수행하여, 그 자식 노드를 새로운 루트로 만들고 기존의 루트 노드를 그 자식 노드의 좌측 자식으로 이동시킨다. 두 번째 단계에서는 불균형이 발생한 노드에 대해 **Right Rotation** 을 수행하여, 첫 번째 회전에서 새롭게 루트가 된 노드를 최종적으로 루트로 승격시키고, 기존의 루트 노드를 그 노드의 우측 자식으로 이동시킨다. 이 과정을 통해 트리의 균형이 회복된다.


### RL Case (Right-Left) {#rl-case--right-left}

RL Case는 \\(HF(v)=-2, HF(v\_{right})=+1\\) 인 경우로, 그림[[5](#figure--fig:avl-rl-case)]와 같다. 그림과 같이 특정 노드에서의 자식 노드들의 높이 차이가 -2로 불균형 하며, 또한 그 우측 자식 노드의 균현 계수가 +1인 경우이다. 즉, 특정 노드의 우측, 그리고 그 노드의 좌측 자식 노드로 인해 불균형이 발생한 경우로 볼 수 있다.

<a id="figure--fig:avl-rl-case"></a>

{{< figure src="/ox-hugo/avl_rl_subtrees_rotation.png" caption="<span class=\"figure-number\">Figure 5: </span>AVL 트리의 LR 케이스에서의 불균형과 회전 과정" >}}

그림 [[5](#figure--fig:avl-rl-case)]의 좌측 크림은 RL 케이스에서의 불균형을 보여주는 그래프이다. 빨간 **불균형이 발생한 노드** 는 우측 노드와 그 노드의 좌측 자식 노드로 인해 불균형이 발생했다. RL 케이스 또한 단일 회전으로 해결되지 않으며, 두 단계의 회전이 필요하다. 첫 번째 단계에서는 불균형이 발생한 노드의 우측 자식 노드에 대해 **Right Rotation** 을 수행하여, 그 자식 노드를 새로운 루트로 만들고 기존의 루트 노드를 그 자식 노드의 우측 자식으로 이동시킨다. 두 번째 단계에서는 불균형이 발생한 노드에 대해 **Left Rotation** 을 수행하여, 첫 번째 회전에서 새롭게 루트가 된 노드를 최종적으로 루트로 승격시키고, 기존의 루트 노드를 그 노드의 좌측 자식으로 이동시킨다. 이 과정을 통해 트리의 균형이 회복된다.


## <span class="org-todo todo STRT">STRT</span> AVL Tree의 구현 {#avl-tree의-구현}


### 군형 계수(Balance Factor) 구현 {#군형-계수--balance-factor--구현}

\\[
BF(v) := h(v\_{\text{left}}) - h(v\_{\text{right}})
\\]
균형 계수는 AVL Tree의 각 노드에서 그 노드의 좌측 자식 노드의 높이에서 우측 자식 노드의 높이를 뺀 값으로 정의된다. 이 균형 계수를 통해 각 노드의 균형 상태를 판단할 수 있으며, AVL Tree는 이 균형 계수가 -1, 0, +1 중 하나인 경우에만 균형이 유지된다고 간주한다. 균형 계수가 +2 또는 -2가 되는 경우에는 트리가 불균형하다고 판단하여 회전 연산을 수행하여 균형을 회복해야 한다. 따라서 AVL Tree의 각 노드는 다음의 구조체로 정의했다.

```c
typedef struct bst_node {
	void *data;
	struct bst_node *left;
	struct bst_node *right;
} bst_node;
```


### 회전(Rotation) 연산 구현 {#회전--rotation--연산-구현}


### 삽입(Insortion) 연산 구현 {#삽입--insortion--연산-구현}


### 탐색(Searching) 연산 구현 {#탐색--searching--연산-구현}


### 삭제(Deleting) 연산 구현 {#삭제--deleting--연산-구현}


## <span class="org-todo todo TODO">TODO</span> 성능 분석 {#성능-분석}


## <span class="org-todo todo TODO">TODO</span> 총정리 {#총정리}

AVL Tree는 기존의 스스로 높이 균형을 유지하는, 즉 각 노드의 자식 노드들의 높이 차이가 1 이하로 유지되는 이진 탐색 트리의 한 종류이다. AVL Tree는 균형 계수(Balance Factor)를 통해 각 노드의 균형 상태를 판단하며, 균형이 깨지는 경우에는 회전 연산을 통해 트리의 균형을 회복한다. 회전 연산은 단일 회전과 이중 회전으로 나뉘며, 각각의 불균형 케이스에 따라 적절한 회전을 선택하여 수행한다.

이번 글은 AVL Tree의 균형 계수와 회전 연산에 대해 작성되었다. 다음 글은 이를 통한 AVL 트리의 실제 구현과 동작, 성능을 비교해보고자 한다. 더 나가아 AVL Tree의 높이의 점근적 상한 또한 수학적으로 유도해보고자 한다.

## References

<div class="csl-bib-body">
  <div class="csl-entry"><a id="citeproc_bib_item_1"></a>
    <div class="csl-left-margin">[1]</div><div class="csl-right-inline">G. Adelson-Velsky and E. M. Landis, “An algorithm for the organization of information,” <i>Soviet mathematics doklady</i>, vol. 3, pp. 1259–1263, 1962, <a href="https://zhjwpku.com/assets/pdf/AED2-10-avl-paper.pdf">https://zhjwpku.com/assets/pdf/AED2-10-avl-paper.pdf</a></div>
  </div>
  <div class="csl-entry"><a id="citeproc_bib_item_2"></a>
    <div class="csl-left-margin">[2]</div><div class="csl-right-inline">Wikipedia contributors, “Avl tree –- Wikipedia, the free encyclopedia,” 2026. <a href="https://en.wikipedia.org/w/index.php?title=AVL_tree&oldid=1340699903">https://en.wikipedia.org/w/index.php?title=AVL_tree&#38;oldid=1340699903</a></div>
  </div>
</div>
