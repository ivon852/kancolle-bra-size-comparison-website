 
# 艦娘乳圖鑑(偽) KanColle Bra Size Comparison

《艦娘乳図鑑》的簡略複製品。


## 1. 如何閱覽本網站

至[Releases](https://github.com/ivon852/kancolle-bra-size-comparison-website/releases)下載最新版zip檔案，解壓縮，以瀏覽器開啟`index.html`即可閱覽網站。

或者手動生成：

1. 複製此儲存庫
```bash
git clone https://github.com/ivon852/kancolle-bra-size-comparison-website.git
```

2. 安裝[Hugo](https://github.com/topics/hugo)

3. 生成靜態HTML。成品位於`public`目錄，用瀏覽器開啟`indexl.html`即可瀏覽。
```bash
hugo --gc --minify
```


## 2. 專案進度

遊戲立繪更新至2023/2/14。

- 支援複合條件搜尋 (未完成)
- 點選縮圖後顯示全身圖 (未完成)
- 深海棲艦 (完成)
- 艦娘 (完成)


## 3. 標示原則

艦娘和深海棲艦的罩杯大小為主觀認定，參考其他出版物作調整。

參考優先度：遊戲立繪 > 季節限定立繪 > Arcade版3D模型 > 動畫版 > 其他官方出版物。不採用二創設定。

艦娘改造後罩杯應相同。深海棲艦有明確的對應艦娘，雙方罩杯也應相同。

被衣物遮擋的預設視為A罩杯。


## 4. 原始資料處理流程

1. 安裝[Hugo](https://github.com/topics/hugo)、[ImageMagick](https://imagemagick.org/index.php)、[Git](https://git-scm.com/)、[GIMP](https://www.gimp.org/)

2. 複製本儲存庫
```bash
git clone https://github.com/ivon852/kancolle-bra-size-comparison-website.git
```

3. 下載kcwiki提供的艦隊Collection的[最新完整遊戲快取](https://ivonblog.com/posts/kccacheproxy-usage/)，解壓縮。

4. 從目錄`kcs2/resources/ship/character_up_dmg/`複製出艦娘的半身像(忽略季節限定立繪)

5. 使用ImageMagick指令，批次裁圖為250x250像素圖片。大部分艦娘的胸部應位於圖片正中央，視情況再手動裁圖。
```bash
mogrify -format png -gravity center -crop 250x250+0+0 -resize 250x250 *.png
```

6. 深海棲艦沒有半身像，因此從`kcs2/resources/ship/full/`目錄複製出全身像(同艦種不同數值的不納入，例如集積地棲姬II、集積地棲姬III)，手動用GIMP裁切為250x250像素圖片。

7. 移動到此儲存庫的`content/posts/`目錄，在個別文章目錄下新增`thumbnails`目錄，將裁切的圖片放到這裡。

8. 在該`thumbnails`目錄新增與圖片同名，後綴為`.meta`的描述檔案，填入罩杯、艦種、是艦娘還是深海棲艦、名字。
```json
{
"Tags": ["Cup: E", "BB", "Kanmusu"],
"Title": "Colorado改",
"ImageDescription": ""
}
```

9. 用Hugo指令生成網頁。成品位於`public`目錄
```bash
hugo --gc --minify
```

## 5. 此網站使用的開源元件

- [Hugo](https://github.com/topics/hugo)
- [SimpLog Hugo Theme](https://github.com/michimani/simplog)
- [hugo-shortcode-gallery](https://github.com/mfg92/hugo-shortcode-gallery)
