#Git官方教程: https://git-scm.com/book/zh/v1/
## Git 分支相关

主支: master

---

### git 提交相关操作

#### 为了不让每次提交操作暴毙，按照[git 官方](https://git-scm.com/book/zh/v1/Git-%E5%9F%BA%E7%A1%80-%E8%AE%B0%E5%BD%95%E6%AF%8F%E6%AC%A1%E6%9B%B4%E6%96%B0%E5%88%B0%E4%BB%93%E5%BA%93)方式进行提交操作

你可能还需要忽略 log，tmp 或者 pid 目录，以及自动生成的文档等等。要养成一开始就设置好 .gitignore 文件的习惯，以免将来误提交这类无用的文件。

```
$ cat .gitignore
*.[oa]
*~
```

文件 .gitignore 的格式规范如下：

1. 检查当前文件状态:  
   `git status`
1. 跟踪新文件:  
   &nbsp; &nbsp;使用命令 `git add` 开始跟踪一个新文件。所以，要跟踪 README 文件，运行：  
   `git add <文件名/add. >`
1. 查看看跟踪状态：  
   `git status`
1. 查看已暂存和未暂存的更新:  
   `git diff --cached`
1. 提交更新:  
   现在的暂存区域已经准备妥当可以提交了。在此之前，请一定要确认还有什么修改过的或新建的文件还没有 git add 过，否则提交的时候不会记录这些还没暂存起来的变化。所以，每次准备提交前，先用 git status 看下，是不是都已暂存起来了，然后再运行提交命令 git commit：  
   `git commit -m`  
   记住，提交时记录的是放在暂存区域的快照，任何还未暂存的仍然保持已修改状态，可以在下次提交时纳入版本管理。每一次运行提交操作，都是对你项目作一次快照，以后可以回到这个状态，或者进行比较。
1. 跳过使用暂存区域:  
   尽管使用暂存区域的方式可以精心准备要提交的细节，但有时候这么做略显繁琐。Git 提供了一个跳过使用暂存区域的方式，只要在提交的时候，给 git commit 加上 -a 选项，Git 就会自动把所有已经跟踪过的文件暂存起来一并提交，从而跳过 git add 步骤：
1. 移除文件:  
    如果需要移除文件 则使用:  
   `git rm`
1. 移动文件
   如果需要移动文件:  
    `git mv from to`

---


### git 修改

1. 修改最后一次提交:  
   `git commit --amend`
1. 取消已经暂存的文件:  
   `git rest HEAD`
1. 取消对文件的修改:  
   `git checkout -- benchmarks.rb`
1. 修改多个提交说明:  
   `git rebase -i`提供一个参数，指明你想要修改的提交的父提交，例如 HEAD~2 或者 HEAD~3。可能记住~3 更加容易，因为你想修改最近三次提交；但是请记住你事实上所指的是四次提交之前，即你想修改的提交的父提交。
---

### git log 相关

- 查看提交历史：  
  `git log`
- 查看提交历史并展开显示每次提交的内容差异：  
  `git log -p`
- 仅显示简要的增改行数统计：  
  `git log --stat`
- 用行方式显示更新历史 　`--pretter=online` (显示方式:单行)  
  `git log --pretter=online`
- 用 foramt 方式显示提交历史 (可常用，优于 git log,)
  %h: 简短的哈希字符串
  %an: 作者
  %ad: 作者修订日期 具体日期
  %s: 提交生命
  `git log --pretty=format:"%h - %an, %ad : %s"`
- 分支演化情况:  
  `git log --pretty=format:"%h %s" --graph`
- 分支演化情况（详细）:  
  `git log --oneline --graph --decorate --all`
- 列出近期更新情况:  
  注意： 你可以给出各种时间格式，比如说具体的某一天（“2008-01-15”），或者是多久以前（“2 years 1 day 3 minutes ago”）。  
  `git log --since=2.weeks`
---

### 远程仓库使用

1. 查看当前的远程库:  
   `git remote`
1. 添加远程仓库：  
   `git remote add [shortname] [url]：`
1. 要抓取所有远程仓库有的有的，但本地仓库没有的信息：  
   `git fetch pb`
1. 从远程仓库抓取数据：  
   `git fetch [remote-name]`
1. 推送数据到远程仓库：
   `git push origin master`
1. 查看远程仓库信息：  
   `git remote show [remote-name] `
1. 远程仓库的重命名：  
   `git remote rename pb paul`
1. 远程仓库的删除：  
   `git remote rm paul`
---

### git 打标签

1. 列显示已有的标签:  
   `git tag`  
   标签的申明： 显示的标签按字母顺序排列，所以标签的先后并不表示重要程度的轻重。
   我们可以用特定的搜索模式列出符合条件的标签。在 Git 自身项目仓库中，有着超过 240 个标签，如果你只对 1.4.2 系列的版本感兴趣，可以运行下面的命令：  
   `git tag -l 'v1.4.2.*'`
1. 新建标签：
   `git tag <tag-name>`
1. 含附注的标签:  
   `git tag -a v1.4 -m 'my version 1.4'`
1. 签署标签:  
   `git tag -s v1.5 -m 'my signed 1.5 tag'`
1. 验证标签:  
   `git tag -v [tag-name]`

### git 分支操作

1. 分支的新建:  
    `git checkout -b iss53`  
    相当于：  
   `git branch iss53`
   `git checkout iss53`

1. 分支的切换：  
   `git checkout [branch-name]`
1. 分支的合并:  
   `git checkout master`  
   `git merge iss53`  
   这个操作是找到 iss53 和 master 的共同祖先，并且跟 iss53 master 两者祖先进行的一次差异化更新操作。
1. 分支的删除:  
   `git branch -d [branch-name]`
1. 遇到冲突时的分支合并:

   ```
   git merge iss53
   Auto-merging index.html
   CONFLICT (content): Merge conflict in index.html
   Automatic merge failed; fix conflicts and then commit the result.
   ```

   使用`git status`进行查阅操作

   如果你想用一个有图形界面的工具来解决这些问题，不妨运行：  
   `git mergetool`
   不同的系统建议使用不同的图形化界面解决

1. 对比分支差异:  
   `git diff branch1 branch2 --stat`(仅文件名)

----