# 用 JavaScript 完成设计模式

## 目标

1. 完成基础的设计模式.
1. 利用 typescript 或者 es6 的方式来实现.
1. 代码可用,结构合理.
1. 设计模式应用场景和解析

---

### 工厂模式 Facotry

作用: 将多种类的生成交给工厂类类来进行,将复杂的操作交给一个工厂类来处理.  
运用:　现在的判定条间是根据名字进行筛选，之后可以根据条件．比如：　我需要一个重量在100-200g的球,可以在`create(name)`中添加业务逻辑进行扩展
```typescript
//工厂生产球类产品
class BallFactory {
  private name: String;
  //未验证: ts是否支持将构造器私有化
  private constructor() {
  }
  //规定了工厂生产的产品必须是球类,
  create(name): ball {
    if (name == "football") {
      return new Football();
    }
    if (name == "basketball") {
      return new Basketball();
    }
  }
}
//球类通用接口
interface ball {
  price: Number;
  run(): void;
}
class Football implements ball {
  price: Number = 100;
  run() {
    console.log("this ball can run");
  }
}
class Basketball implements ball {
  price: Number = 100;
  run() {
    console.log("this basketball can run");
  }
}

```

---

### 迭代器模式 Iterator

### 适配器模式 Adapter

### 单例模式 Singleton

### 原型模式 Prototype

### 构建模式 Builder

### 抽象工厂

### 桥接模式

### Stragegy

### Composite

### 装饰器模式 Decorator

### Vistor

### 责任链 ChainOfResponsibility

### Facade

### Mediator

### 观察者模式 Observer

### Memeto

### Stat

### Flyweight

### Proxy

### Command

### Interperter
