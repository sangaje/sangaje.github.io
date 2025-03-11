---
layout: post
title: "[GPU Computing #1] 병렬 컴퓨팅의 기초"
description: 4-1 수업 인 GPU Computing을 정리하기 위한 글
image: "/assets/img/post_images/4-1/GPU Computing.png"
category: [수업정리, GPU 컴퓨팅]
tags: [GPU, 병렬연산, 최적화]
math: true
mermaid: true
comments: true
---

# GPU 병렬 컴퓨팅 (Parallel Computing)
```mermaid
classDiagram
    class IAnimal {
        <<interface>>
        +makeSound()
    }
    class Dog {
        +bark()
    }
    IAnimal <|.. Dog
```