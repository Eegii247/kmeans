# encoding: utf-8
"""
@author: lee
@file: prediction_test.py
@desc: python3环境 Metis0.3
"""
from time_series_detector import detect

if __name__ == '__main__':
    # 异常例子
    data = {
        "dataC": "660,719,649,674,672,683,679,642,758,777,731,791,776,692,724,665,698,644,691,651,710,650,576,591,589,639,655,620,678,619,620,608,604,618,598,617,584,542,584,625,548,575,607,570,555,630,571,536,547,501,518,522,496,526,526,499,527,488,479,454,541,541,501,546,523,584,538,554,540,501,541,486,551,507,571,644,534,508,544,484,502,573,551,543,546,554,560,573,493,536,548,508,488,475,531,515,520,477,547,573,546,504,537,520,524,551,515,468,548,555,564,579,542,535,573,635,594,475,484,539,520,516,542,522,519,507,550,528,525,500,467,525,591,551,536,640,590,575,516,546,630,656,556,579,556,606,574,544,603,607,667,666,571,533,489,536,552,522,599,569,581,565,552,581,621,614,642,562,559,635,680,622,591,655,642,648,633,626,627,717,737,637,630,606,698,635,652,611,700,727,670,695,682,735,684,674,673,664,783,672,702,697,636,595,690,686,750,652,677,702,704,689,734,769,756,737,672,694,678,792,687,717,712,718,744,690,672,708,707,708,717,750,679,728,916,874,814,850,754,770,711,670,699,679,694,677,714,691,652,694,685,685,716,672,681,677,709,676,670,638,710,734,774,694,732,741,725,787,750,720,747,746,800,755,759,748,750,763,720,746,792,708,739,678,665,686,791,745,742,736,720,786,727,700,732,725,735,753,685,712,732,669,709,709,688,717,750,703,738,742,691,687,694,820,753,708,749,778,737,647,690,764,811,727,721,727,658,694,738,803,759,674,766,746,730,746,700,720,747,702,721,654,699,714,742,789,740,763,709,707,797,650,719,672,741,672,703,709,686,664,776",
        "dataB": "610,574,560,532,599,527,541,580,572,546,560,584,554,572,544,559,512,527,536,586,582,563,578,562,526,546,575,511,549,502,520,525,524,560,568,550,556,529,532,537,600,550,537,527,517,590,576,548,551,553,549,574,507,501,520,514,587,528,504,517,505,569,521,547,515,690,767,610,575,549,561,569,589,543,515,570,552,490,560,571,582,521,518,472,514,547,512,542,583,557,535,577,551,542,595,500,557,545,502,548,532,534,547,534,524,539,530,566,552,578,589,599,541,564,575,552,574,644,504,562,571,615,566,528,594,569,551,563,524,557,566,639,633,600,576,566,603,578,554,559,580,554,578,567,564,613,566,592,633,584,606,567,564,583,611,557,548,577,528,555,571,618,599,560,570,567,551,544,553,633,617,562,593,586,573,617,611,553,557,556,555,585,586,570,549,536,542,569,585,653,593,623,547,544,578,604,599,603,590,608,599,603,562,527,576,587,501,630,564,613,583,586,588,601,617,644,625,646,605,598,578,599,590,602,601,549,571,566,584,598,617,627,652,667,603,575,633,565,596,570,581,636,678,670,590,597,626,628,694,638,618,578,617,570,611,577,634,552,560,591,615,562,636,611,579,589,593,618,591,602,600,589,584,591,605,623,621,605,596,564,526,601,598,645,565,582,606,555,554,604,591,620,578,621,618,594,618,629,596,610,606,566,567,593,564,540,597,551,580,544,622,606,559,571,609,598,643,571,634,610,554,603,627,645,616,560,578,564,670,585,663,614,605,595,598,613,636,591,619,588,597,521,618,647,597,601,579,634,626,562,632,605,633,560,581,557,584,600,573,551,621",
        "dataA": "753,706,762,721,728,737,796,756,745,722,717,702,693,741,733,675,731,821,955,745,765,781,740,680,691,686,642,681,627,674,729,741,691,653,629,627,644,642,695,643,603,614,598,632,597,567,578,582,613,620,597,573,551,525,514,528,502,528,504,512,473,542,544,560,591,549,564,550,491,482,530,490,537,535,563,568,525,535,485,542,551,529,481,517,518,521,554,525,508,577,564,575,568,548,546,511,523,549,564,585,576,582,559,566,527,569,534,519,545,548,521,596,574,569,587,578,534,570,650,580,551,601,560,612,609,586,551,560,568,593,641,589,549,564,566,545,578,543,610,578,625,625,628,693,746,627,605,583,586,655,613,618,672,670,634,617,584,574,609,613,620,641,620,608,645,635,674,645,632,661,682,772,843,818,953,953,970,961,989,1014,997"
    }
    # 正常例子
    # data = {
    #     "dataC": "114389185,114234173,115527986,116200888,116464945,115521825,115429673,114796526,113914980,115626404,115547821,113885417,114743695,115711092,115495893,115134357,115640012,115369734,114017863,114720372,115911618,114713033,114517883,115423603,116727793,115391822,115057138,115853808,114902252,114924479,115495599,115876207,114539971,113365006,115310696,114654996,112531883,113281313,112862446,113106511,114068948,112499687,112492489,111654993,113173258,113923092,113085818,112833722,113860316,114068458,113207928,114267722,114349986,113795874,114156174,115594661,115586246,114487976,115270879,115089434,114687302,115245478,114624937,112705049,110388754,111746861,113110515,112325115,112312777,112301329,111570511,111030138,112440859,112574175,113073430,113629842,114726429,112907457,110708885,112569623,112996043,112566384,112359041,113624798,113967221,113638330,115112582,115822993,114974694,114898355,115310441,114259536,114214718,115192033,115930813,115083607,115108077,115419117,114679551,115335808,116034800,114889923,114898470,114387863,115288280,114561352,112723290,112968823,112409194,111330526,111596977,112053845,111735318,109803318,110993701,111861244,109559514,108781007,109233220,108244468,107230495,109487660,108718971,106956507,108304778,108916726,107075854,105286271,106334479,107491329,106080414,105259583,106461229,105252944,105393992,105604513,104470451,102990073,102193551,103377917,103091719,102284188,102865445,102456714,101612947,102723708,102046149,101365975,100613366,101959809,101673567,101385185,102213527,102561969,103043582,102036988,102533176,102234465,101566617,102214658,102718433,101934777,101125022,102028742,102392328,101186683,101042924,101229669,99477407,100049068,101306623,100993350,101562131,101965321,102941557,102875097,102812488,103521909,102530765,102453308,103143393,104007317,104184226,102568246,104433436,104852333,103426023,102744900,102384940,102982328,101515359,102416268,103559861,102371477,103641154,103795346,103169684,102526625,103295551,103004052,103042520,104198534,105049028,104427142,104786691,105831201,104621554,103049306,103325128,104796677,104954773,104166564,104678634,104624244,104813874,105031728,104220038,103434030,101932870,103797174,104748780,104162936,104216781,105188421,105988308,105517938,106151874,106863651,105845539,106306436,107623318,106311949,106080447,106803893,107474414,107516945,108558010,108477801,106555108,106384009,107288256,107589313,107919192,107181975,108193101,108582140,107578282,107619852,107547021,106745777,107384247,108023854,108139581,106890808,108553054,108786931,108328956,109145938,109373173,109076644,107663115,108978931,109655034,108499752,108738445,109873477,109382382,108355442,109243834,109677052,108645561,109984704,110244045,110745015,110868344,111698258,111865222,110041159,109959518,111218280,110362763,109447832,111164789,111195059,111545113,112282379,112479462,111732605,111195127,113301828,113469559,112048281,112662998,113744872,113134489,112002028,113382510,113044311,112079082,112954937,113791977,113368923,113370797,113484135,113794057,113008463,113443730,114361685,113723715,113695255,115106112,114730496,115090114,115469354,116479338,116054006,115001770,115681897,115243883,115158446,115495057,115039559,115152107,114608693,116663441,115768329,115221973,115581010,115924545,116000621,115428597,115576863,115910284,115437874,116243564,116848174,116019628,114892513,115810225,115879175,115815867,115911137,117178797,116386309,116565858,117219815,117275961,115526687,117298773,119334093,119538578,118808894,120589809,120906866,119808187,121139885,122095046,120652575,119767325,121826353,121830090",
    #     "dataB": "119666915,119913210,120675263,120763862,120575287,121430910,121781131,121392134,120649490,121743487,121542934,119985382,122515392,123314019,123412869,122459691,122147012,122108244,123053649,125205243,125432455,124009403,124977580,126263929,125419583,123522858,124306277,124072458,123058663,122172453,123351119,122125600,121928665,122887189,123557560,123304525,122317785,122092175,122404252,122768138,121907759,122530252,122617000,121971311,123486929,123629716,122163290,122890684,123291131,124412382,123791060,124197245,125346167,124421053,125573888,126225177,125360536,124375933,124417709,125484208,124694997,125539940,125418903,124859588,123437271,124700422,126271130,124268045,125917614,129413091,130035026,128252009,129618906,129863131,128964286,127981040,127481150,126781716,126561021,128681225,127841301,126165945,127885285,129340671,129366986,128222348,128776874,128384329,127899322,130306981,130921104,129749467,128793371,129469312,129895610,128712024,129123427,129135275,128791431,129061103,129956532,129488172,129391371,129348152,130538367,129845129,128914692,130333125,130106616,129100273,129338948,129452583,129447273,128306599,130238226,129520083,126080374,126185772,126049551,126135178,125310324,126853777,126276553,125094332,124664697,124027382,123402636,122573253,123076897,123216479,122582326,122212279,123554219,123750141,123442170,124037297,123254399,121426974,121572064,122701268,121702313,120863240,122740216,121903717,121073114,121234314,121210894,121148647,120092665,122058779,121364790,119939839,120854898,120002366,121229049,119844256,120115785,120026648,118079829,119616388,120291590,118402040,117353202,119461591,119358416,117665679,118318309,118617320,117054601,117605102,118429516,117154886,116986185,116792250,118730573,118022720,116169317,116609970,117412885,117003917,117051828,117890910,117120416,116420329,118372762,116816557,114946274,115923672,115866519,115171041,114920559,115386711,115449065,114339739,116261885,115609553,114448334,114010653,115165076,115560107,114144576,114851704,115863370,114739065,114482681,115188734,114580929,113368166,114325715,115157807,114326296,113329262,114603550,114470665,113758862,113440232,114166470,114003147,112470740,114893900,113813955,111879969,113366281,115137266,114428777,113694417,114559100,113982307,112632717,114427268,113917227,112950706,113272852,113192973,114351585,113106878,112844690,113193882,113037473,112848357,113006586,113668941,112581372,113325873,114630569,113024168,111884719,113532289,112278213,111800028,112701967,112592776,112696050,112131845,114654299,113232019,111709316,112302793,112151523,112344641,112378146,112381410,112020733,111727090,112783288,112828876,111704534,110428381,111304131,112773568,111279441,111648064,114208311,113459293,112628127,113698595,112572392,111213817,111919511,113432610,115215493,114892593,116675841,115778827,115866455,116480098,116151344,114967193,114479477,116187695,115592166,114912048,116899754,117679367,117147440,116383093,116973012,116025964,115303365,116338743,117073767,117554156,116882210,117560377,117521010,116099606,116894009,117482747,116191199,116763324,117462837,115591552,116333967,118434351,119339640,117535955,115007009,115601156,115197594,114552659,114089143,115221092,115082676,114516265,115821551,116440717,113685864,113824729,114658419,114970231,112189372,114640357,114371036,113853926,114508246,113765454,114066253,112779631,113622567,114807568,117106357,117276192,117892689,116242986,115836773,117729397,117671950,116940147,117495103,119491282,118242611,116204127,117716533,117636794,116957596,117300628,116947295,117032057,117316508,119838866,118655829",
    #     "dataA": "111419833,112072024,114111830,114928334,115018261,114100014,115432842,114103136,112466335,114226925,114643605,112613053,113788319,113650269,112706262,112507764,113051628,113099353,111482402,112679154,113224997,112536681,113166614,113577936,113703362,112620729,112934047,113970782,113272216,112029996,113785230,113277878,111585126,112089708,112664186,111566577,110464642,111580075,110837812,110631029,110433038,109904708,110319175,110366512,111313257,111072393,110009422,111259583,111777740,111960046,111009567,111530551,111680628,111708250,112867703,112333224,112323413,111619011,113001227,113093125,110781552,111434248,110412116,108806336,107912521,108770241,111344473,110300485,109834933,109373920,107704803,106374404,108395128,108393515,107874466,108290046,109497936,108354013,107694347,109271610,109243326,107894746,110063786,110723438,110791001,110364764,111770048,111178441,110324486,111488030,111494532,110918916,111021476,111841035,111734436,110964079,110993168,111404043,110507050,110267040,111657890,110835274,110458151,110262909,111306738,110500510,109288389,110302726,109514753,108535153,109079051,109086639,108543004,106601753,107902121,107381342,105581044,105685604,106129306,105187226,104396333,106630914,106723039,104990490,106181059,105859886,104135755,102738217,103393519,103687698,101968926,102101594,103002865,102193179,101730927,102727108,101879527,100736158,100057710,100675386,99843038,98203919,100241686,100400065,99571221,100324861,99927782,98641661,98160979,99832807,100086661,98941615,99911623,100524058,100311718,98822311,99646428,99451605,97116761,98906793,100218813,98709789,99294293,100259431,100877207,99363766,99603209,99511654,99010762,98641627,99814803,98786820,99063100,99121283,101853906,100539423,99581190,100661441,100737796,100200998,101771966"
    # }
    detect_obj = detect.Detect()
    # 率值检测
    # print(detect_obj.rate_predict(data))
    # 量值检测
    print(detect_obj.value_predict(data))