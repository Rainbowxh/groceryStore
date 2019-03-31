# 用 JavaScript 完成设计模式

## 目标

1. 完成基础的设计模式.
1. 利用 typescript 或者 es6 的方式来实现.
1. 代码可用,结构合理.
1. 设计模式应用场景和解析

---

### 工厂模式 Facotry

作用: 将多种类的生成交给工厂类类来进行,将复杂的操作交给一个工厂类来处理.  
运用:　现在的判定条间是根据名字进行筛选，之后可以根据条件．比如：　我需要一个重量在 100-200g 的球,可以在`create(name)`中添加业务逻辑进行扩展

```typescript
//工厂生产球类产品
class BallFactory {
  private name: String;
  //未验证: ts是否支持将构造器私有化
  private constructor() {}
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


#### es5中的迭代器
```js
function IteratorInstance(items) {
  let i = 0;
  return {
    next: function() {
      let done = i >= items.length;
      let value = !done ? items[i++] : undefined;
      return {
        value: value,
        done: done
      };
    }
  };
}

let iterator = IteratorInstance(arr);
iterator.next();
iterator.next();
iterator.next();
iterator.next();
```



### 适配器模式 Adapter

### 单例模式 Singleton

作用: 全局只有唯一实例  
运用: SpringBoot,全局唯一接口  
实现: Java双重锁实现,js实现,以及typescript中的实现

- java 中的经典实现

```java
public class Singleton{
    //私有化构造函数
    private Singleton(){}
    //保证singleton在被操作时候顺序,可见性
    private volatile static Singleton singleton;
    public staic Singleton getInstance() {
        if(singleton == null){
            //同步锁:其作用的范围是synchronized后面括号括起来的部分，作用主的对象是这个类的所有对象。保证其他线程访问时候阻塞
            synchronized(Sinleton.class){
                if(singleton == null){
                    singleton = new Singleton();
                }
            }
        }
        return singleton;
    }
}
```

```js
//这样的写法我认为是不太好的,依旧使用Singleton能够实例化
function Singleton() {
  this.name = "Singleton";
}
let getInstance = (function() {
  let instance;

  return function() {
    if (!instance) {
      instance = new Singleton();
    }
    return instance;
  };
})();
```

```typeScript
class Singleton {
    private static singleton: Singleton;
    private constructor() {

    }
    public static getInstance() {
        if(!Singleton.singleton){
            Singleton.singleton = new Singleton();
        }
        return Singleton.instance;
    }
}
```

---

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
