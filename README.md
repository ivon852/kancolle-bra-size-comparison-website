 
# 艦娘乳圖鑑(偽) KanColle Bra Size Comparison

《艦娘乳図鑑》的簡略複製品。

線上瀏覽：[https://kancollebra.netlify.app/](https://kancollebra.netlify.app/)


## 0. 專案進度

遊戲立繪更新至2023/2/14。

- 支援複合條件搜尋 (未完成)
- 點選縮圖後顯示全身圖 (未完成)
- 深海棲艦 (完成)
- 艦娘 (完成)


## 1. 標示原則

艦娘和深海棲艦的罩杯大小為主觀認定，參考其他出版物作調整。

參考優先度：遊戲立繪 > 季節限定立繪 > Arcade版3D模型 > 動畫版 > 其他官方出版物。不採用二創設定。

艦娘改造後罩杯應相同。深海棲艦有明確的對應艦娘，雙方罩杯也應相同。

被衣物遮擋的預設視為A罩杯。


## 2. 原始資料處理流程

1. 下載艦隊Collection的[最新完整遊戲快取](https://shizuru.piro.moe/kccp/)，解壓縮。

2. 從目錄`kcs2/resources/ship/character_up_dmg/`抽出艦娘的半身像(忽略季節限定立繪)，使用ImageMagick裁圖為250x250像素圖片。大部分圖片的胸部應位於正中央，視情況再手動裁圖。
```bash
mogrify -format png -gravity center -crop 250x250+0+0 -resize 250x250 *.png
```

3. 深海棲艦沒有半身像，因此從`kcs2/resources/ship/full/`目錄抽出全身像(同艦種不同數值的不納入，例如集積地棲姬II、集積地棲姬III)，手動裁切為250x250像素圖片。

4. 移動到此儲存庫的`content/posts/`目錄，在個別文章目錄下新增`thumbnails`目錄，將裁切的圖片放到這裡。

5. 在該`thumbnails`目錄新增與圖片同名，後綴為`.meta`的描述檔，填入罩杯、艦種、是艦娘還是深海棲艦、名字。

6. 使用`deploy_n.sh`指令稿部署網站。


## 3. 離線存取此網站

1. 複製此儲存庫
```bash
git clone https://github.com/ivon852/kancolle-bra-size-comparison-website.git
```

2. 安裝[Hugo](https://github.com/topics/hugo)

3. 於本機執行伺服器，以`http://localhost:1313`網址存取。
```bash
hugo server -D
```

## 4. 此網站使用的開源元件

- [Hugo](https://github.com/topics/hugo)
- [SimpLog Hugo Theme](https://github.com/michimani/simplog)
- [hugo-shortcode-gallery](https://github.com/mfg92/hugo-shortcode-gallery)
