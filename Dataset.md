## Dataset

The Chinese Ancient Rubbing and Manuscript Character Dataset (ARMCD) is a novel dataset designed for the Automated Chinese Ancient Character Restoration (ACACR) task. It comprises 15,553 real-world ancient single-character images sourced from 42 rubbings and manuscripts. These artifacts span the period from 200 to 1800 AD and encompass the works of over 200 calligraphy artists. To our knowledge, ARMCD represents the largest publicly available ACACR dataset, surpassing existing counterparts in both the diversity of source artifacts and the quantity of images.

![image-20231217175911655](https://github.com/marchlion1/DIffACR_private/raw/main/figure/concept.png)

**Real**: original single-character images
**Pred**: preprocessed images
**Mask**: mask images
**Synd**: synthesized images

**Please visit the link below, fill out the application form, and download our dataset.**

## Data Collection

Rubbings and manuscripts serve as vital carriers of Chinese cultural heritage and historical information (Qiu 2023), extensively utilized across disciplines such as art, archaeology, historiography, and cultural studies. The ARMCD dataset is curated from **42 authoritative and representative Chinese ancient rubbings and manuscripts**, comprising **15,093 intact ancient Chinese character images** and **460 degraded character samples**. These materials document the works of over 200 calligraphy artists spanning from the Wei-Jin period (3rd-5th century) to the Qing Dynasty (1636–1912 AD).

*The quantitative distributions of character samples across historical periods are presented in the charts below.*

https://github.com/marchlion1/DIffACR_private/blob/main/figure/dynasty.png



The data sources of **uneroded** characters are listed in the table below. 

<!-- | Work                                                         |    Script     |  Type   |  Calligrapher  |    Dynasty    | Count |
| :----------------------------------------------------------- | :-----------: | :-----: | :------------: | :-----------: | :---: |
| *Four Hundred and Ninety-Six Characters from the Southern Tang Dynasty (南唐四百九十六字)* |    Regular    |   Ink   |  Zhao Zhiqian  |     Qing      |  512  |
| *Copybook of Shantang Poetry (山堂诗帖)*                     | Semi-cursive  |   Ink   |   Cai Xiang    | Northern Song |  75   |
| *The Record of the Rebuilt of Taoist Trinity Hall of Xuanmiao Temple (玄妙观重修三门记)* |    Regular    |   Ink   |  Zhao Mengfu   |     Yuan      |  562  |
| *Eulogy to the Portrait of Dongfang Shuo (东方朔画赞)*       |    Regular    | Rubbing |  Yan Zhenqing  |     Tang      |  587  |
| *Inscription on Mount Dizhu (砥柱铭)*                        | Semi-cursive  |   Ink   | Huang Tingjian | Northern Song |  228  |
| *Poem on the Hall of Wind and Pines (松风阁)*                | Semi-cursive  |   Ink   | Huang Tingjian | Northern Song |  105  |
| *Ode on Leisurely Living (闲居赋)*                           | Semi-cursive  |   Ink   |  Zhao Mengfu   |     Yuan      |  600  |
| *Song on an Ancient Light-Transmitting Mirror (麻徵君透光古镜歌)* | Semi-cursive  |   Ink   |   Xianyu Shu   |     Yuan      |  167  |
| *Copybook of Returning to Anqiu Garden (归安丘园帖)*         | Semi-cursive  |   Ink   |     Su Shi     | Northern Song |  68   |
| *Copybook of Snow Cold (雪寒帖)*                             | Semi-cursive  |   Ink   | Huang Tingjian | Northern Song |  40   |
| *Handscroll of Du Fu's Autumn Meditations (杜甫秋兴诗卷)*    | Semi-cursive  |   Ink   |  Zhao Mengfu   |     Yuan      |  275  |
| *Zihui Hall Rubbing Album of the Ling Fei Jing*              | Small regular |         |                |               | 2479  |
| *The Rubbing Album of the Record of Miaoyan Temple in Huzhou* |               |         |                |               |  657  |
| *The Rubbing Album of the Bestowal to Xiang Ju*              |               |         |                |               |  28   |
| *The Poems of Sun Miao*                                      |               |         |                |               |  74   |
| *The Poem of the Morning of the Palace*                      |               |         |                |               |  53   |
| *The Rubbing Album of the Record of Fushen Temple in Hangzhou* |               |         |                |               |  769  |
| *The Rubbing Album of the Declaration Scroll*                |               |         |                |               |  233  |
| *The Rubbing Album of the Inscription of Zuiwengting Ji*     |               |         |                |               |  391  |
| *The Copybook of Memorial on Dispatching the Troops*         |               |         |                |               |  671  |
| *The Rubbing Album of Stele for Danba the Emperor's Teacher by Zhao Mengfu* |               |         |                |               |  850  |
| *Goddess of the River Luo in Running Script by Zhao Mengfu*  |               |         |                |               |  707  |
| *The Song of Double Pines*                                   |               |         |                |               |  191  |
| *The Calligraphy Copybook of Self-reflection*                |               |         |                |               | 1037  |
| *A Calligraphic Model-book from the Imperial Archives in the Chunhua Era* |               |         |                |               | 2409  |
| *The Calligraphy Copybook of Nong Fang Poems*                |               |         |                |               |  31   |
| *Dong Ming Imperial Commendation in Regular Script by Jiang Ligang* |               |         |                |               |  115  |
| *The Record of Huaiyun Garden in Gunshan*                    |               |         |                |               |  448  |
| *Song Dynasty Rubbing Album of the Word of Teaching Disciples* |               |         |                |               |  234  |
| *The Rubbing Album of the Record of Restoration of Three Fates of Xuanmiao Temple* |               |         |                |               |  497  | -->

| Work                                                         |     Script     |   Type   |   Calligrapher    |    Dynasty     | Count |
| :----------------------------------------------------------- | :------------: | :------: | :---------------: | :------------: | :---: |
| *Four Hundred and Ninety-Six Characters from the Southern Tang Dynasty (南唐四百九十六字)* |    Regular     |   Ink    |   Zhao Zhiqian    |      Qing      |  512  |
| *Copybook of Shantang Poetry (山堂诗帖)*                     | Semi-cursive   |   Ink    |     Cai Xiang     | Northern Song  |  75   |
| *The Record of the Rebuilt of Taoist Trinity Hall of Xuanmiao Temple (玄妙观重修三门记)* |    Regular     |   Ink    |   Zhao Mengfu     |      Yuan      |  562  |
| *Eulogy to the Portrait of Dongfang Shuo (东方朔画赞)*       |    Regular     | Rubbing  |   Yan Zhenqing    |      Tang      |  587  |
| *Inscription on Mount Dizhu (砥柱铭)*                        | Semi-cursive   |   Ink    |  Huang Tingjian   | Northern Song  |  228  |
| *Poem on the Hall of Wind and Pines (松风阁)*                | Semi-cursive   |   Ink    |  Huang Tingjian   | Northern Song  |  105  |
| *Ode on Leisurely Living (闲居赋)*                           | Semi-cursive   |   Ink    |   Zhao Mengfu     |      Yuan      |  600  |
| *Song on an Ancient Light-Transmitting Mirror (麻徵君透光古镜歌)* | Semi-cursive   |   Ink    |    Xianyu Shu     |      Yuan      |  167  |
| *Copybook of Returning to Anqiu Garden (归安丘园帖)*         | Semi-cursive   |   Ink    |      Su Shi       | Northern Song  |  68   |
| *Copybook of Snow Cold (雪寒帖)*                             | Semi-cursive   |   Ink    |  Huang Tingjian   | Northern Song  |  40   |
| *Handscroll of Du Fu's Autumn Meditations (杜甫秋兴诗卷)*    | Semi-cursive   |   Ink    |   Zhao Mengfu     |      Yuan      |  275  |
| *Zihui Hall Rubbing Album of the Ling Fei Jing*              | Small regular  | Rubbing  |     Zhong Yao     | Three Kingdoms | 2479  |
| *The Rubbing Album of the Record of Miaoyan Temple in Huzhou* |    Regular     | Rubbing  |   Zhao Mengfu     |      Yuan      |  657  |
| *The Rubbing Album of the Bestowal to Xiang Ju*              | Semi-cursive   | Rubbing  |      Mi Fu        | Northern Song  |  28   |
| *The Poems of Sun Miao*                                      | Semi-cursive   |   Ink    |      Su Shi       | Northern Song  |  74   |
| *The Poem of the Morning of the Palace*                      | Semi-cursive   |   Ink    |   Zhao Mengfu     |      Yuan      |  53   |
| *The Rubbing Album of the Record of Fushen Temple in Hangzhou* |    Regular     | Rubbing  |   Zhao Mengfu     |      Yuan      |  769  |
| *The Rubbing Album of the Declaration Scroll*                |    Cursive     | Rubbing  |     Huai Su       |      Tang      |  233  |
| *The Rubbing Album of the Inscription of Zuiwengting Ji*     |    Regular     | Rubbing  |      Su Shi       | Northern Song  |  391  |
| *The Copybook of Memorial on Dispatching the Troops*         | Semi-cursive   |   Ink    |   Zhao Mengfu     |      Yuan      |  671  |
| *The Rubbing Album of Stele for Danba the Emperor's Teacher by Zhao Mengfu* |    Regular     | Rubbing  |   Zhao Mengfu     |      Yuan      |  850  |
| *Goddess of the River Luo in Running Script by Zhao Mengfu*  | Semi-cursive   |   Ink    |   Zhao Mengfu     |      Yuan      |  707  |
| *The Song of Double Pines*                                   | Semi-cursive   |   Ink    |   Zhao Mengfu     |      Yuan      |  191  |
| *The Calligraphy Copybook of Self-reflection*                |    Regular     | Rubbing  |   Yan Zhenqing    |      Tang      | 1037  |
| *A Calligraphic Model-book from the Imperial Archives in the Chunhua Era* |    Multiple    | Rubbing  |     Various       | Northern Song  | 2409  |
| *The Calligraphy Copybook of Nong Fang Poems*                | Semi-cursive   | Rubbing  |      Mi Fu        | Northern Song  |  31   |
| *Dong Ming Imperial Commendation in Regular Script by Jiang Ligang* |    Regular     |   Ink    |   Jiang Ligang    |      Qing      |  115  |
| *The Record of Huaiyun Garden in Gunshan*                    |    Regular     | Rubbing  |   Wen Zhengming   |      Ming      |  448  |
| *Song Dynasty Rubbing Album of the Word of Teaching Disciples* | Semi-cursive   | Rubbing  |    Wang Xizhi     |      Jin       |  234  |
| *The Rubbing Album of the Record of Restoration of Three Fates of Xuanmiao Temple* |    Regular     | Rubbing  |   Zhao Mengfu     |      Yuan      |  497  |



The data sources of **eroded** characters are listed in the table below. 

<!-- | Work                                                         |    Script     |  Type   | Calligrapher |    Dynasty    | Count |
| ------------------------------------------------------------ | :-----------: | :-----: | :----------: | :-----------: | :---: |
| *A Calligraphic Model-book from the Imperial Archives in the Chunhua Era (淳化阁帖)* |    Various    | Rubbing |   Various    | Northern Song |  54   |
| *Free Life Pond Stele (放生池碑)*                            |    Regular    | Rubbing | Yan Zhenqing |     Tang      |  45   |
| *Yellow Court Classic (黄庭经)*                              | Small regular | Rubbing | Wen Zhenming |     Ming      |  10   |
| *The Rubbing Album of the Nine Songs*                        |               | Rubbing |              |               |  17   |
| *Confucius Temple Stele (孔子庙堂碑)*                        |    Regular    | Rubbing |  Yu Shinan   |     Tang      |  64   |
| *Yan Qinli Stele (颜勤礼碑)*                                 |    Regular    | Rubbing | Yan Zhenqing |     Tang      |  50   |
| *Sanxitang Studio’s Calligraphic Model-book (三希堂法帖)*    |    Various    | Rubbing |   Various    |     Qing      |  60   |
| *Epitaph of Shi Wan (石婉墓志)*                              |    Regular    | Rubbing |  Anonymous   | Northern Wei  |  30   |
| *Stele of Songgaoling Temple in Zhongyue Mountain (嵩高灵庙碑)* |    Regular    | Rubbing |  Anonymous   | Northern Wei  |  100  |
| *Stele of Xuanmi Pagoda (玄秘塔碑)*                          |    Regular    | Rubbing | Liu Gongquan |     Tang      |  30   | -->

| Work                                                         |    Script     |  Type   |   Calligrapher    |    Dynasty     | Count |
| :----------------------------------------------------------- | :-----------: | :-----: | :---------------: | :-----------: | :---: |
| *A Calligraphic Model-book from the Imperial Archives in the Chunhua Era (淳化阁帖)* |    Various    | Rubbing |      Various      | Northern Song |  54   |
| *Free Life Pond Stele (放生池碑)*                            |    Regular    | Rubbing |   Yan Zhenqing    |      Tang      |  45   |
| *Yellow Court Classic (黄庭经)*                              | Small regular | Rubbing |   Wen Zhengming   |      Ming      |  10   |
| *The Rubbing Album of the Nine Songs*                        | Semi-cursive  | Rubbing |   Zhao Mengfu     |      Yuan      |  17   |
| *Confucius Temple Stele (孔子庙堂碑)*                        |    Regular    | Rubbing |    Yu Shinan      |      Tang      |  64   |
| *Yan Qinli Stele (颜勤礼碑)*                                 |    Regular    | Rubbing |   Yan Zhenqing    |      Tang      |  50   |
| *Sanxitang Studio’s Calligraphic Model-book (三希堂法帖)*    |    Various    | Rubbing |      Various      |      Qing      |  60   |
| *Epitaph of Shi Wan (石婉墓志)*                              |    Regular    | Rubbing |    Anonymous      | Northern Wei  |  30   |
| *Stele of Songgaoling Temple in Zhongyue Mountain (嵩高灵庙碑)* |    Regular    | Rubbing |    Anonymous      | Northern Wei  |  100  |
| *Stele of Xuanmi Pagoda (玄秘塔碑)*                          |    Regular    | Rubbing |   Liu Gongquan    |      Tang      |  30   |
