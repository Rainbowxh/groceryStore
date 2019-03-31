class Observe {
  constructor(data) {
    this.data = data;
    this.walk(data);
  }
  walk(data) {
    let self = this;
    //判断是否还需要监听子组件
    if (!data || typeof data !== "object") {
      return;
    }
    Object.keys(data).map(key => {
      let value = data[key];
      self.defineReative(data, key, value);
    });
  }
  defineReative(data, key, value) {
    //添加容器
    let dep = new Dep();
    let child = new Observe(value);
    Object.defineProperty(data, key, {
      get: function() {
        if (Dep.target) {
          dep.addSub(Dep.target);
        }
        return val;
      },
      set: function(newVal) {
        if (val === newVal) {
          return;
        }
        val = newVal;
        dep.notify();
      }
    });
  }
}

class Dep {
  constructor() {
    this.subs = [];
  }
  addSub(watcher) {
    this.subs.push(watcher);
  }
  notify() {
    let arr = Array.from(this.subs);
    arr.forEach(watcher => {
      watcher.update();
    });
  }
}

export default Observe;
