<template>
  <div>
    <canvas id="charts" width="320" height="380"></canvas>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
/**
 * Entity space
 */

interface coordinate {
  x: number;
  y: number;
}
enum directions {
  Up,Right,Fown,Left
}
@Component({})
export default class snake extends Vue {
  canv: any;
  snake_array: Array<coordinate>;
  snake_size: number = 5;
  snake_direction: string[] = ["up", "right", "down", "left"];
  score: number;
  cell_width: number = 5;
  tx: any;
  ty: any;
  canv_width: number;
  canv_height: number;
  direction: any;
  run: any;
  realdirecton: directions;
  //初始化数据
  public init():void {
    this.direction = this.snake_direction[1];
    this.canv = <HTMLCanvasElement>document.getElementById("charts");
    this.canv_width = this.canv.width;
    this.canv_height = this.canv.height;
    this.score = 0;
    this.generate_snake();
    this.generate_target();
    this.bind_evnets();
    this.run = setInterval(this.draw, 100); 
  }
  //生成蛇的数组
  public generate_snake():void {
    this.snake_array = [];
    for (let i = 0; i < this.snake_size; i++) {
      this.snake_array.push({
        x: i,
        y: 0
      });
    }
  }
  //生成目标函数
  public generate_target():void{
    console.log(this.canv_width);
    console.log(this.canv_height);
    this.tx = Math.round(
      (Math.random() * (this.canv_width - this.cell_width)) / this.cell_width
    );
    this.ty = Math.round(
      (Math.random() * (this.canv_height - this.cell_width)) / this.cell_width
    );
  }
  public draw():void{
    let ctx = this.canv.getContext("2d");
    let head_cell;
    let nx, ny, splice_i;
    let hit;
    console.log(this.tx);
    console.log(this.ty);
    // 绘制画布
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, this.canv_width, this.canv_height);
    //绘制边界
    ctx.strokeStyle = "black";
    ctx.strokeRect(0, 0, this.canv_width, this.canv_height);
    // 绘制目标
    ctx.fillStyle = "red";
    ctx.strokeStyle = "red";
    ctx.fillRect(
      this.tx * this.cell_width,
      this.ty * this.cell_width,
      this.cell_width,
      this.cell_width
    );
    ctx.strokeRect(
      this.tx * this.cell_width,
      this.ty * this.cell_width,
      this.cell_width,
      this.cell_width
    );
    //贪吃蛇的头部定位
    head_cell = this.snake_array[this.snake_array.length - 1];
    let head_x = head_cell.x;
    let head_y = head_cell.y;

    //移动定位
    switch (this.direction) {
      case this.snake_direction[0]:
        nx = head_cell.x;
        ny = head_cell.y + 1;
        break;
      case this.snake_direction[1]:
        nx = head_cell.x + 1;
        ny = head_cell.y;
        break;
      case this.snake_direction[2]:
        nx = head_cell.x;
        ny = head_cell.y - 1;
        break;
      case this.snake_direction[3]:
        nx = head_cell.x - 1;
        ny = head_cell.y;
        break;
    }
    //碰撞检测
    if(nx*ny<0){
        return
    }
    if (nx === this.tx && ny === this.ty) {
      this.score++;
      this.snake_array.push({
        x: this.tx,
        y: this.ty
      });
    }
    this.snake_array.splice(0,1);
    this.snake_array.push({
      x: nx,
      y: ny
    });
    //画蛇
    ctx.fillStyle = "blue";
    ctx.strokeStyle = "white";
    for (var i = 0; i < this.snake_array.length; i++) {
      ctx.fillRect(
        this.snake_array[i].x * this.cell_width,
        this.snake_array[i].y * this.cell_width,
        this.cell_width,
        this.cell_width
      );
      ctx.strokeRect(
        this.snake_array[i].x * this.cell_width,
        this.snake_array[i].y * this.cell_width,
        this.cell_width,
        this.cell_width
      );
    }
  }
  public bind_evnets():void {
    let vm = this;
    document.onkeydown = function(e) {
      let code = e.which,
        index;
      switch (code) {
        case 37: //left
          if (vm.direction !== "right") {
            vm.direction = "left";
          }
          break;
        case 38: //down
          if (vm.direction !== "up") {
            vm.direction = "down";
          }
          break;
        case 39: //right
          if (vm.direction !== "left") {
            vm.direction = "right";
          }
          break;
        case 40: //up
          if (vm.direction !== "down") {
            vm.direction = "up";
          }
          break;
        default:
          return;
      }
    };
  }
  mounted() {
    this.init();
    this.draw();
  }
}
</script>

<style lang="less" scoped>
#charts {
  border: 1px solid orange;
}
</style>

