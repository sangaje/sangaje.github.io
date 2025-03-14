---
layout: post
title: "[Airsim] 드론 시뮬레이터 기초"
description: 해당 글은 Airsim을 활용하고, 공부하기에 앞서 드론 시뮬레이터에 대한 개념과 기타 기본 개념들을 정리해 본 것이다.
image: "/assets/img/post_images/Drone/Drone Simulator.png"
category: [드론, 시뮬레이터]
tags: [드론, 시뮬레이터, Airsim, 에어심]
math: true
mermaid: true
comments: true
---

## 무인 항공기(Unmanned Aerial vehicle, UAV)와 드론(Drone)

무인 항공기는 무인기라고도 불리며 말 그대로 사람이 타지 않는 항공기 혹은 멀티콥터(Multicopter)의 일종이다. 우리는 우크라이나-러시아 전쟁에 대한 뉴스를 접하면서 전쟁에서도 이러한 드론을 활용한다는 얘기를 심심치 않게 듣는다. 또한 미국에선 넓은 농장에 농약을 치는 용도로도 31%에 다라고, 비록 시범 운영이지만 중국에서는 시골 마을에 물류를 배달하기 위해 드론 공항을 설치, 활용하여 활용하고 있다고 하니 드론이 이제 우리 일상생활에 더욱 깊이 들어올 것을 체감할 수 있다.

무인 항공기, 즉 드론을 우리는 조종기를 통해 4개의 로터(Rotor, 회전 날개)에 의해 비행하는 쿼드콥터(Quadcopter)을 주로 생각하기 쉽다. 하지만 실제로 드론은 큰 범주일 뿐이며 이러한 퀴드콥터는 드론의 한 일종일 뿐이다. 예시로 광안리나 한강에서 요즘 인기 있는 드론쇼의 경우 각각의 드론을 조종하지는 않지만, 지정된 경로를 따라 자동으로 주행하는 드론이다. 그리고 미국에서 사용하는 MQ-1C 그레이 이글과 같이 비행기처럼 생겼지만 내부 조종사 없이 정찰 임무를 수행하는 경우도 이러한 드론에 해당한다. 심지어 탑승자 없이 수중에서 임무를 수행하거나 조종하는 수중 드론(UUV, Underwater Drone)도 있다. 미국 해군을 위해 보잉이 개발한 XLUUV(eXtra Large Uncrewed Undersea Vehicle) 인 오르카가 수중 드론의 대표적 예시이다.

<center> MQ-1C 그레이 이글 </center>

![MQ-1 그레이 이글](/assets/img/post_images/Drone/Simulator/Airsim/MQ-1C_Warrior_(2005-08-11).jpg) 

<center> By Photo Courtesy of U.S. Army - <a class="external free" href="https://en.wikipedia.org/wiki/File:OCPA-2005-08-11-080331.jpg">http://en.wikipedia.org/wiki/File:OCPA-2005-08-11-080331.jpg</a> </center>

<center> 오르카 XLUUV </center>

![오르카](/assets/img/post_images/Drone/Simulator/Airsim/orca-final-prep.jpeg)

<div style="text-align: center;">
  사진 출처 - <a href="https://www.boeing.com/defense/xluuv#gallery" target="_blank">보잉 공식 사이트</a>
</div>

드론에 대한 대략적인 감은 잡힌 것 같다. 그렇다면 드론의 정의는 무엇일까? 위키피디아에는 드론을 
`"실제 조종사가 직접 탑승하지 않고, 지상에서 사전 프로그램된 경로에 따라 자동(auto) 또는 반자동(semi-auto)으로 비행하는 비행체, 탑재임무장비(payload), 지상통제장비(GCS: ground control system or station), 통신장비(데이터 링크: data link), 지원장비(support equipment) 및 운용인력(operators)의 전체 시스템"`
을 통칭한다고 정의하고 있다.

## Reference

1. 위키피디아, [무인 항공기](https://ko.wikipedia.org/wiki/%EB%AC%B4%EC%9D%B8_%ED%95%AD%EA%B3%B5%EA%B8%B0)
1. 박찬식, [[박기자's 스마트팜 클로즈업] 농업용 드론이 불러올 농업 혁신](https://www.smartfn.co.kr/news/articleView.html?idxno=93167)  , (2019.07.29)
1. 위키피디아, [UUV](https://en.wikipedia.org/wiki/Unmanned_underwater_vehicle)
1. 유효정, [드론, 중국대륙을 날다…“200km까지 배송"](https://zdnet.co.kr/view/?no=20170907095905), (2017.09.07)
1. 보잉, [XLUUV](https://www.boeing.com/defense/xluuv#overview)
1. 위키피디아, [MQ-1C 그레이 이글](https://ko.wikipedia.org/wiki/MQ-1C_%EA%B7%B8%EB%A0%88%EC%9D%B4_%EC%9D%B4%EA%B8%80)