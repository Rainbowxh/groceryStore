class Watcher {
  constructor(vm, exp, cb) {
    this.vm = vm;
    this.exp = exp;
    this.cb = cb;
    this.value = this.get();
  }
  get() {
    Dep.target = this;
    //执行观察者
    let value = this.vm.data[this.exp];
    Dep.target = null;
    return value;
  }
  update() {
    this.run();
  }
  run() {
    let value = this.get();
    let oldValue = this.value;
    if (value !== oldValue) {
      this.value = value;
      this.cb.call(this.vm, value, oldValue);
    }
  }
}

export default Watcher;
