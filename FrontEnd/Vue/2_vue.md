# Single-File Components
-----------------
# Component
- UI를 독립적이고 재사용 가능한 일부분으로 분할하고, 각 부분을 개별적으로 다룰 수 있음
- Vue에서의 Single File Component는 <template>, <script>, <style>로 구성되어 있음.
  - 각 component는 <script setup> 블록을 하나만 포함할 수 있으며 이는 setup() 함수로 사용된다.
  - <style>은 여러가지 태그가 포함될 수 있으며, scoped가 지정되면, 현재 컴포넌트에만 적용된다.
  
# Node Package Manager
- NPM
- Node.js 의 기본 패키지 관리자

# Module, Module의 한계
- 개발하는 앱 크기가 커지고 복잡해지면서 파일 하나에 모든 기능을 담기 어려워짐
- 따라서 자연스럽게 파일을 여러 개로 분리하여 관리를 하게 되었고, 이때 분리된 각 파일이 바로 모듈
----------------
- 하지만 처리해야하는 JS 모듈의 개수도 극적으로 증가해, 병목현상 발생, 의존성 문제 등 발생
  - Bundler을 통해 이를 해결하고자 함.

# Bundler
- 여러 모듈과 파일을 하나 (혹은 여러개)의 번들로 묶어 최적화하여 앱에서 사용할 수 있게 만들어주는 도구
- 의존성 관리, 코드 최적화, 리소스 관리 등..

# Vue Project 구조
## node_modules
- Node.js 프로젝트에서 사용되는 외부 패키지들이 저장되는 디렉토리
- 의존성 모듈 저장, 관리
- 프로젝트 실행 시 필요한 라이브러리와 패키지들을 포함
- .gitignore에 작성됨

## package-lock.json
- 패키지 설치에 필요한 모든 정보를 포함
- 협업 과정, 서버 환경의 일관성 있는 의존성에 도움
- npm install을 통해 패키지를 설치할 때, 명시된 버전과 의존성을 기반으로 설치

## package.json
- 프로젝트 메타 정보, 의존성 패키지 목록 포함
- package-lock.json과 함께 의존성 관리 및 버전 충돌 및 일관성 유지 역할

## public 디렉토리
- 소스코드에 참조되지 않는, 항상 같은 이름을 갖는, import할 필요 없는 정적파일들을 중심적으로 위치시킴
- 항상 root 절대경로를 사용하여 참조.

## src 디렉토리
- 프로젝트의 주요 소스코드 포함
- 라우팅, 스타일, 컴포넌트 ... 핵심!
### src - asset
- 컴포넌트 자체에서 참조하는 내부 파일을 저장하는 데 활용 (스타일 시트, 폰트, 이미지 ...)
- 컴포넌트가 아닌 곳에선 public 디렉토리에 위치한 파일 사용

### src - App.vue
- Vue 앱의 최상위 Root 컴포넌트
- 다른 하위 컴포넌트들을 포함

### src - main.js
- Vue 인스턴스를 생성하고, 애플리케이션을 초기화하는 역할
- 필요한 라이브러리를 import 하고 전역 설정을 수행

### src - index.html
- Vue 앱의 기본 html
- 앱의 진입점
- App.vue가 해당 페이지에 mounted
- 필요한 스타일 시트, 스크립트 등의 외부 리소스를 로드할 수 있음 (bootstrap ...)

# Virtual DOM
- 가상의 DOM을 메모리에 저장하고, 실제 DOM과 동기화 하는 프로그래밍 개념
- 실제 DOM과의 변경 사항 비교를 통해, 변경된 부분만 실제 DOM에 적용하는 방식

## Virtual DOM의 장점
- 효율성 : DOM 조작 최소화, 변경된 부분만 업데이트 => 성능 향상
- 반응성 : 데이터의 변경을 감지, Virtual DOM을 효율적으로 갱신해 UI를 자동으로 업데이트
- 추상화 : 개발자는 실제 DOM조작을 Vue 에게 맡기고 컴포넌트와 템플릿을 활용하는 추상화된 프로그래밍 방식으로 원하는 UI 구조를 구성하고 관리할 수 있음.
## Virtual DOM 주의사항!
- 실제 DOM에 직접 접근 금지!
  - querySelector, createElement, addEventListener 등
- ref() 와 Lifecycle Hooks 함수 (onMounted, onUpdate ...) 활용할 것
```html
<input ref="input">
```
```js
const input = ref(null)
// ref값과 변수명 일치할 것
```
-----------------
# props, emit
- 부모 => 자식 : pass props
- 자식 => 부모 : emit event

## props 특징
- 부모 속성이 업데이트 되면, 자식으로 전달되지만, 그 역은 불가능
- 자식 컴포넌트 내부에서 props를 변경하려고 시도해서는 안되며, 불가능
- 또한 부모 컴포넌트가 업데이트될 때마다 이를 사용하는 자식 컴포넌트의 props가 최신 값으로 업데이트 된다.
  - => 부모 컴포넌트에서만 변경하고 이를 내려받는 자식 컴포넌트는 자연스럽게 갱신
### 단방향인 이유
- 데이터 흐름의 일관성 및 단순화

### props 선언
- 부모가 되는 component에 자식 component import
```
App.vue에 Parent.vue import
Parent.vue에 ParentChild.vue import
```
- Parent에서 ParentChild.vue에 보낼 props를 작성하는 방법?
```html
<template>
  <div>
    <ParentChild my-msg="message" />
    // Parent.vue에서 작성
  </div>
</template>
```
- Props 선언
```js
// 1. 문자열 배열을 사용한 선언
defineProps({
  myMsg: String
})
// ParentChild.vue에서 작성
// html은 대소문자를 구별하지 못하기에, 대문자를 소문자로 바꾸고 앞에 - 를 붙히는 문법 사용 (부모 component에서 전달할 때)
// 자식으로 전달 시 (kebab-case), 선언 및 템플릿 참조 (camelCase)
```
```html
{{ myMsg }}
```

### 정리
1. 부모
- js : import 자식, html : <자식 send-something = "message" />
2. 자식
- js : defineProps ({ sendSomething: 데이터타입 }), html : {{ sendSomething }}
  - 손자에게 이어서 전달하는 경우엔 html : <자식 :send-something = "sendSomething" /> ... v-bind필요!
3. 손자
- js : defineProps ({ sendSomething: 데이터타입 }), html : {{ sendSomething }}

#### 위 예시는 ref값을 전달하는 과정이 아니지만, ref값 전달도 크게 다르지 않음 (v-bind를 활용할 것)
--------------------
## $emit()
- 자식 컴포넌트가 이벤트를 발생시켜 부모 컴포넌트로 데이터를 전달하는 역할의 메서드
  - $는 Vue 인스턴스의 내부 변수를 가리킨다. (life cycle hooks, 인스턴스 메서드 등에 접근할 때 사용)
---------------------
# emit, props ... 예시로 학습하자.
```html
// Baby
<template>
    <div>
        <h1>Baby</h1>
        {{ myMsg }}
        <button @click="$emit('someEvent')">someEvent emit</button>
        <button @click="myDefineEmit">DefineEmit</button>
        <button @click="myDefineEmit2">Send Args</button>
    </div>
</template>

<script setup>
defineProps({ myMsg:String })

const emit = defineEmits(['someEvent', 'emitArgs'])

const myDefineEmit = function () {
    emit('someEvent')
}
const myDefineEmit2 = function () {
    emit('emitArgs', 1,2,3)
}
</script>

<style scoped>

</style>
```
```html
// Parent
<template>
    <div>
        {{ myMsg }}
        <Baby  
            @some-event="someCallback"  :my-msg="myMsg" 
            @emit-args="getNumbers"
        />
    </div>
</template>

<script setup>
import Baby from '@/components/Baby.vue'

defineProps({
    myMsg:String
})

const someCallback = function () {
    console.log('Baby의 emit 수신')
}

const getNumbers = function (...args) {
    console.log(args)
    console.log(`Baby가 보낸 추가 인자 ${args} 수신`)
}
</script>

<style scoped>

</style>
```
## emit의 Naming
- 선언 및 발신 : camelCase
- 수신 : kebab-case
