 
# 艦娘乳圖鑑(偽) KanColle Bra Size Comparison

《艦娘乳図鑑》的迫真複製品。

艦娘和深海棲艦的乳量大小為主觀認定＋參考動畫版做調整。


立繪更新至2023/2/14。


## 1. 進度

- 深海棲艦 (完成)
- 艦娘 (未完成)


## 2. 資料處理流程

1. 下載艦隊Collection的[完整遊戲快取](https://shizuru.piro.moe/kccp/)。

2. 從目錄`kcs2/resources/ship/character_up_dmg/`抽出艦娘的半身像，使用ImageMagick裁圖為250x250圖片：
```bash
mogrify -format png   -gravity center -crop 250x250+0+0 -resize 250x250  *.png
```

3. 深海棲艦沒有半身像，從`kcs2/resources/ship/full/`目錄抽出全身像(重複艦種，僅數值不同的不納入，例如集積地棲姬II、集積地棲姬III)，手動裁切為250x250大小圖片。

4. 將裁切的圖片放置到此儲存庫的`content/posts/kancolle-bra-size-comparison/thumbnails/`目錄。

5. 在該目錄下新增與檔案同名，後綴為`.meta`的描述檔，填入乳量、艦種、是艦娘還是深海棲艦、艦娘名字。

6. 使用`deploy_n.sh`指令稿部署網站。


## 3. 網站使用的開源元件

- [Hugo](https://github.com/topics/hugo)
- [SimpLog Hugo Theme](https://github.com/michimani/simplog)
- [hugo-shortcode-gallery](https://github.com/mfg92/hugo-shortcode-gallery)
