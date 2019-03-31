import Observe from "./observe";
import Watcher from "./watcher";

class selfValue {
  constructor(data, el, exp) {
    let self = this;
    this.data = data;
    Object.keys(data).map(key => {
      self.proxyKeys(key);
    });
    let observe = new Observe(data);
    el.innerHtml = this.data[exp];
    new Watcher(this, exp, value => {
      el.innerHtml = value;
    });
    return this;
  }
  proxyKeys(keys) {
    let slef = this;
    Object.defineProperty(this, key, {
      enumerable: false,
      configurable: true,
      get: function proxyGetter() {
        return self.data[key];
      },
      set: function proxySetter(newVal) {
        self.data[key] = newVal;
      }
    });
  }
}

function nodeToFragment(el) {
  let fragment = document.createDocumentFragment();
  let child = el.firstChild;
  while (child) {
    fragment.appendChild(child);
    child = el.firstChild;
  }
  return fragment;
}

class compileElement {
  constructor(el) {
    let childNodes = el.childNodes;
    let self = this;
    [].slice.call(childNodes).forEach(node => {
      let reg = /\{\{(.*)\}\}/;
      let text = node.textContent;
      if (this.isElentNode(node)) {
        this.compileNode(node);
      } else if (self.isTextNode(node) && reg.test(text)) {
        let ctx = reg.exec(text)[1];
        this.compileText(node, ctx);
      }

      if (node.childNodes && node.childNodes.length) {
        compileElement(el);
      }
    });
  }
  compile(node) {
    let nodeVal = node.attributes;
    let self = this;
    Array.prototype.forEach.call(noeVal, ele => {
      //todo logical
    });
  }
  compileText(node, exp) {
    new Watcher()....
  }
}
