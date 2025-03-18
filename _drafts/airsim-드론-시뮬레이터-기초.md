---
layout: post
title: "[Airsim] 드론 시뮬레이(Drone Simulator)터 기초"
description: 해당 글은 Airsim을 활용하고, 공부하기에 앞서 드론 시뮬레이터에 대한 개념과 기타 기본 개념들을 정리해 본 것이다.
image: "/assets/img/post_images/Drone/Drone Simulator.png"
category: [드론, 시뮬레이터]
tags: [드론, 시뮬레이터, Airsim, 에어심]
math: true
mermaid: true
comments: true
---

## 무인 항공기(Unmanned Aerial vehicle, UAV)와 드론(Drone)

무인 항공기는 무인기라고도 불리며 말 그대로 사람이 타지 않는 항공기이다. 우리가 흔히 드론 하면 떠올리는 멀티콥터(Multicopter)가 이러한 무인 항공기의 일종이다[^1]. 우리는 우크라이나-러시아 전쟁에 대한 뉴스를 접하면서 전쟁에서도 이러한 드론을 활용한다는 얘기를 심심치 않게 듣는다. 또한 미국에선 넓은 농장에 농약을 치는 용도로도 드론을 응용할 것이라고 답변하는 사람이 31%에 다라고[^2], 비록 시범 운영이지만 중국에서는 시골 마을에 물류를 배달하기 위해 드론 공항을 설치, 활용하여 활용[^3]하고 있다고 하니 드론이 이제 우리 일상생활에 더욱 깊이 들어올 것을 체감할 수 있다.

드론을 우리는 조종기를 통해 4개의 로터(Rotor, 회전 날개)에 의해 비행하는 쿼드콥터(Quadcopter)을 주로 생각하기 쉽다. 하지만 실제로 드론은 큰 범주일 뿐이며 이러한 퀴드콥터는 드론의 한 일종일 뿐이다. 예시로 광안리나 한강에서 요즘 인기 있는 드론쇼의 경우 각각의 드론을 조종하지는 않지만, 지정된 경로를 따라 자동으로 주행하는 드론이다. 그리고 미국에서 사용하는 MQ-1C 그레이 이글[^4]과 같이 비행기처럼 생겼지만 내부 조종사 없이 정찰 임무를 수행하는 경우도 이러한 드론에 해당한다. 심지어 탑승자 없이 수중에서 임무를 수행하거나 조종하는 수중 드론(UUV, Underwater Drone)[^5]도 있다. 미국 해군을 위해 보잉이 개발한 XLUUV(eXtra Large Uncrewed Undersea Vehicle) 인 오르카[^6]가 수중 드론의 대표적 예시이다.

<center> MQ-1C 그레이 이글 </center>

![MQ-1 그레이 이글](/assets/img/post_images/Drone/Simulator/Airsim/MQ-1C_Warrior_(2005-08-11).jpg) 

<center> By Photo Courtesy of U.S. Army - <a class="external free" href="https://en.wikipedia.org/wiki/File:OCPA-2005-08-11-080331.jpg">http://en.wikipedia.org/wiki/File:OCPA-2005-08-11-080331.jpg</a> </center>

<center> 오르카 XLUUV </center>

![오르카](/assets/img/post_images/Drone/Simulator/Airsim/orca-final-prep.jpeg)

<div style="text-align: center;">
  사진 출처 - <a href="https://www.boeing.com/defense/xluuv#gallery" target="_blank">보잉 공식 사이트</a>
</div>

이를 통하여 드론은 단순히 우리가 생각하는 쿼드콥터뿐만 아닌 조종사가 없이 이동하는, 즉 무인 이동체를 통칭한다는 것을 알 수 있다. 이제 드론에 대한 대략적인 감은 잡힌 것 같다. 그렇다면 드론의 정의는 무엇일까? 한번 ChatGPT를 통하여 드론의 정의에 관해 물어보았다. ChatGPT는 드론을 `원격 조종 또는 자동 제어 시스템을 통해 운용되는 무인 항공기(UAV, Unmanned Aerial Vehicle)를 의미합니다. 군사, 상업, 산업, 개인 용도로 사용되며, 항공 촬영, 감시, 물류, 농업, 재난 구조 등 다양한 분야에서 활용됩니다. 드론은 일반적으로 프로펠러를 이용해 비행하며, GPS, 센서, 카메라 등의 장비를 탑재할 수 있습니다.` 라고 설명한다. 즉 드론을 무인 이동체(UV)에 속하는 무인 항공기(UAV)로 설명하며 다양한 장비를 장착하여 주로 사용되는 것으로 보인다. 드론은 실제로 무인 항공기를 통칭하기도 하며 앞서 말한 수중 드론(UUV)을 포함하는 것으로 보아 무인 이동체로도 여겨지는 것 같다. 다만 앞으로 이를 공부하는데 있어 뜻이 혼용된다면 어려움이 있을 수 있기에 무인 항공기로 생각하고 알아볼 것이다.

## 무인 이동체(UV, Uncrewed Vehicle or Unmanned Vehicle)

앞서 드론이 뭐고 무인 항공체와 드론이 혼용된다고 알아보았다. 그렇다면 이러한 사람이 안에서 직접 조종하는 것이 아닌 비행체나 차량 잠수정 같은 것들을 뭐라고 할까? 우리는 이러한 것들을 무인 이동체 즉 UV[^7]라고 부른다. 이러한 무인 이동체는 원격으로 제어(Telerobotic Control)할 수 있다. 이때 원격 조종(Remote Controlled) 되거나 그게 아니더라도 다른 방법의 지시를 통하여, 원격으로 움직임을 유도(Remote Guided)할 수 있다. 또한 우리가 이제 꽤나 익숙해진 자동 주행(Autonomously Controlled)이라는 이동체가 스스로 환경을 인지하고 길을 찾아 나가는 방법도 있다.

이러한 무인 이동체는 정말 많은 종류가 있으며 각각의 종류에 대해서도 크기, 용도 등에 따라서 세부적으로 분류되기도 한다. 몇 가지 무인 이동체의 종류에 대해 위키피디아에[^7]선 다음과 같이 정리했다.

- **Remote control vehicle (RC)** : radio-controlled cars 또는 radio-controlled aircraft와 같은 원격 조종 차량이다. 우리가 어릴때 가지고 놀던 RC카가 대표적으로 떠오른다.

- **Unmanned ground vehicle (UGV)** : 자율주행차 또는 무인 전투 차량(Unmanned Combat Ground Vehicles, UCGV)이다. 테슬라는 비록 완전 자율주행차는 아니더라도 이러한 것을 생각해 볼 수 있다.
  - Self-driving truck (자율 주행 트럭)
  - Driverless tractor (무인 트랙터)

- **Unmanned ground and aerial vehicle (UGAV)** : 하이브리드 이동 방식의 무인 차량이다.

- **Unmanned aerial vehicle (UAV)** : 고정익(Fixed-wing, 여객기와 같이 날개가 고정된) 또는 회전익(Rotorwing, 헬리콥터와 같이 날개가 움직여 양력을 얻는) 항공기로 구성된 무인 항공기, 일반적으로 "드론"이라고 불린다.
  - Unmanned combat aerial vehicle (UCAV) : 무인 전투 항공기
  - Medium-altitude long-endurance unmanned aerial vehicle (MALE) : 중고도 장기체공 무인 항공기
  - Miniature UAV (SUAV) : 소형 무인 항공기
  - Delivery drone : 배송용 드론
  - Micro air vehicle (MAV) : 초소형 공중 이동체
  - Target drone : 표적 드론

- **Autonomous spaceport drone ship** : 자율 항공모함 드론 선박이다.

- **Unmanned surface vehicle (USV)** : 수면에서 작동하는 "수면 드론" 또는 "드론 선박"이다.

- **Unmanned underwater vehicle (UUV)** : 수중에서 작동하는 "수중 드론" 또는 "드론 잠수함"이다.
  - Remotely operated underwater vehicle (ROUV) : 원격 조작 수중 이동체
  - Autonomous underwater vehicle (AUV) : 자율 수중 이동체
    - Intervention AUV (IAUV) : 개입형 자율 수중 이동체
    - Underwater glider : 수중 활공 이동체

- **Uncrewed spacecraft** : 원격 조종("무인 우주 임무") 또는 자율 조종("로봇 우주선" 또는 "우주 탐사선") 우주선이다.

따라서 우리가 알아보고자 하는 드론은 주로 무인 항공기에 속하는 것을 알수 있다. 앞으로 알아볼 Airsim에도 이러한 무인 항공기에 대해 각종 센서와 같은 장치, 역학 등을 포함한 시뮬레이션을 제공한다.

## 드론 시뮬레이터(Drone Simulator)와 그 필요성



## Reference

[^1]: 위키피디아, [무인 항공기](https://ko.wikipedia.org/wiki/%EB%AC%B4%EC%9D%B8_%ED%95%AD%EA%B3%B5%EA%B8%B0)

[^2]: 박찬식, [[박기자's 스마트팜 클로즈업] 농업용 드론이 불러올 농업 혁신](https://www.smartfn.co.kr/news/articleView.html?idxno=93167)  , (2019.07.29)

[^3]: 유효정, [드론, 중국대륙을 날다…“200km까지 배송"](https://zdnet.co.kr/view/?no=20170907095905), (2017.09.07)

[^4]: 위키피디아, [MQ-1C 그레이 이글](https://ko.wikipedia.org/wiki/MQ-1C_%EA%B7%B8%EB%A0%88%EC%9D%B4_%EC%9D%B4%EA%B8%80)

[^5]: 위키피디아, [UUV](https://en.wikipedia.org/wiki/Unmanned_underwater_vehicle)

[^6]: 보잉, [XLUUV](https://www.boeing.com/defense/xluuv#overview)


[^7]: 위키피디아, [무인 이동체](https://en.wikipedia.org/wiki/Uncrewed_vehicle)