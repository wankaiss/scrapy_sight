# coding: utf-8

batch1 = [
    u'巴黎',
    u'尼斯',
    u'阿维尼翁',
    u'戛纳',
    u'马赛',
    u'里昂',
    u'卢瓦尔河谷',
    u'普罗旺斯',
    u'蔚蓝海岸',
    u'波尔多',
    u'安纳西',
    u'法兰西岛',
    u'隆河口省',
    u'艾克斯',
    u'沃克吕兹省',
    u'诺曼底',
    u'勃艮第-弗朗什-孔泰大区',
    u'阿尔萨斯',
    u'昂蒂布',
    u'阿尔勒',
    u'第戎',
    u'格拉斯',
    u'斯特拉斯堡',
    u'滨海自由城',
    u'吉伦特省',
    u'夏慕尼白朗峰',
    u'布列塔尼',
    u'圣保罗·德·旺斯',
    u'尼姆',
    u'戈尔德',
    u'科西嘉',
    u'图尔',
    u'洛林',
    u'夏慕尼',
    u'芒什省',
    u'萨尔特',
    u'瓦朗索勒',
    u'鲁昂',
    u'图卢兹',
    u'勒芒',
    u'南特',
    u'依云',
    u'蒙彼利埃',
    u'里尔',
    u'卡尔卡松',
    u'摩泽尔省',
    u'兰斯',
    u'科尔玛',
    u'埃兹',
    u'默尔特-摩泽尔',
    u'格勒诺布尔',
    u'南锡',
    u'利摩日',
    u'阿卡雄',
    u'翁弗勒尔',
    u'梅茨',
    u'丰泰纳德沃克吕瑟',
    u'雷恩',
    u'卡昂',
    u'枫丹白露',
    u'贝瑞',
    u'圣米歇尔山',
    u'吉维尼',
    u'阿雅克肖',
    u'克莱蒙费朗',
    u'土伦',
    u'比亚里茨',
    u'沙特尔',
    u'拉罗谢尔',
    u'布洛瓦',
    u'博讷',
    u'芒通',
    u'普瓦捷',
    u'勒阿弗尔',
    u'谢尔河',
    u'巴斯蒂亚',
    u'圣马洛',
    u'加来',
    u'巴约',
    u'夏朗德',
    u'亚眠',
    u'佩皮尼扬',
    u'昂布瓦兹',
    u'米卢斯',
    u'卢瓦尔省',
    u'莱桑德利',
    u'阿尔比',
    u'布尔日',
    u'圣雷米',
    u'特鲁瓦',
    u'鲁瓦扬',
    u'阿普特',
    u'埃佩尔奈',
    u'尚蒂伊',
    u'波城',
    u'圣雷米',
    u'瓦兹河畔奥维尔',
    u'博尼法乔',
    u'埃特勒塔',
    u'瓦讷',
    u'多维尔',
    u'欧塞尔',
    u'巴约讷',
    u'坎佩尔',
    u'贝桑松',
    u'卡奥尔',
    u'萨瓦及勃朗峰区域',
    u'昂热',
    u'圣艾蒂安',
    u'希农',
    u'滨海布洛涅',
    u'滨海圣洛朗',
    u'阿宰勒里多',
    u'洛什',
    u'干邑',
    u'勒贝克埃卢安',
    u'St-Jean-Cap-Ferrat',
    u'伊瓦尔',
    u'第纳尔',
    u'洛里昂',
    u'拉尼永',
    u'圣布里厄',
    u'沙勒维尔-梅济耶尔',
    u'维朗德里',
    u'卢瓦尔河畔肖蒙',
    u'巴卡拉',
    u'圣Sornin（滨海夏朗德）',
    u'滨海博略',
    u'伏旧',
    u'索恩河畔沙隆',
    u'马孔',
    u'康斯',
    u'冈布桑',
    u'圣特马雷恩德库恩斯',
    u'沙博泰',
    u'萨尔瑟纳',
    u'拉沙佩勒－昂瓦尔戈德马',
    u'莱萨德雷特',
    u'萨尔瑟纳',
    u'布瑞森圣茵诺森',
    u'格埃兹',
    u'瓦莱拉格',
    u'圣特马雷恩德库恩斯',
    u'波利尼',
    u'伯尼索米诺格',
    u'圣特马雷恩德库恩斯',
    u'伊夫哈克',
    u'乌兹',
    u'艾勒弗鲁瓦德',
    u'伯尼索米诺格',
    u'莱萨布雷',
    u'蒙费列叙尔莱',
    u'伯尼索米诺格',
    u'罗马',
    u'威尼斯',
    u'米兰',
    u'佛罗伦萨',
    u'托斯卡纳',
    u'那不勒斯',
    u'拉齐奥',
    u'威尼托',
    u'伦巴第',
    u'西西里岛',
    u'梵蒂冈',
    u'维罗纳',
    u'比萨',
    u'锡耶纳',
    u'都灵',
    u'拉斯佩齐亚',
    u'五渔村',
    u'阿马尔菲海岸',
    u'博洛尼亚',
    u'卡塔尼亚',
    u'庞贝',
    u'撒丁岛',
    u'普利亚',
    u'翁布里亚',
    u'巴勒莫',
    u'阿马尔菲',
    u'卢卡',
    u'圣吉米尼亚诺',
    u'热那亚',
    u'里米尼',
    u'佩鲁贾',
    u'阿格里真托',
    u'维琴察',
    u'帕多瓦',
    u'的里雅斯特',
    u'锡拉库扎',
    u'拉文纳',
    u'贝加莫',
    u'萨莱诺',
    u'布雷西亚',
    u'亚西西',
    u'陶尔米纳',
    u'卡利亚里',
    u'莫德纳',
    u'费拉拉',
    u'卡萨莱蒙费拉托',
    u'帕尔玛',
    u'维亚雷焦',
    u'科莫',
    u'墨西拿',
    u'特拉帕尼',
    u'巴里',
    u'诺托',
    u'波尔查诺',
    u'乌迪内',
    u'里乔内',
    u'马泰拉',
    u'埃尔巴',
    u'卡普里',
    u'帕维亚',
    u'佩斯卡拉',
    u'拉古萨',
    u'索伦托',
    u'皮亚琴察',
    u'安科纳',
    u'阿雷佐',
    u'伊斯基亚',
    u'萨萨里',
    u'维泰博',
    u'塔兰托',
    u'巴萨诺德尔格拉帕',
    u'阿斯蒂',
    u'特伦托',
    u'古比奥',
    u'雷焦艾米利亚',
    u'科尔托纳',
    u'阿尔盖罗',
    u'格罗塞托',
    u'阿尔贝罗贝洛',
    u'马尔萨拉',
    u'波西塔诺',
    u'皮斯托亚',
    u'奥斯塔',
    u'卡塞塔',
    u'穆拉诺',
    u'卡托利卡',
    u'圣雷莫',
    u'普拉托',
    u'阿斯科利皮切诺',
    u'克雷莫纳',
    u'瓦雷泽',
    u'里窝那',
    u'特雷维索',
    u'贝内文托',
    u'奥尔维耶托',
    u'奥特朗托',
    u'蒙特普尔恰诺',
    u'库马约尔',
    u'奇维塔韦基亚',
    u'福尔泰德伊马尔米',
    u'奥斯图尼',
    u'布林迪西',
    u'贾尔迪尼-纳克索斯',
    u'科森扎',
    u'佩萨罗',
    u'夏卡',
    u'蒙扎',
    u'特尔尼',
    u'斯廷蒂诺',
    u'塞尼加利亚',
    u'阿奎泰尔梅',
    u'格雷韦伊恩基亚恩蒂',
    u'米拉佐',
    u'阿尔扎凯纳',
    u'莱切',
    u'福贾',
    u'蒙特卡蒂尼-泰尔梅',
    u'曼托瓦',
    u'瓦斯托',
    u'代森扎诺－德尔加达',
    u'阿奇雷亚莱',
    u'乌尔比诺',
    u'芬奇',
    u'科涅',
    u'希克利',
    u'奥尔比亚',
    u'科尔蒂纳丹佩佐',
    u'莱科',
    u'拉奎拉',
    u'阿巴诺泰尔梅',
    u'萨沃纳',
    u'莱尼亚诺',
    u'塞斯托-圣乔凡尼',
    u'多尔加利',
    u'布斯托-阿西齐奥',
    u'里瓦德尔加尔达',
    u'内镇',
    u'伊塞奥',
    u'圣安蒂奥科',
    u'福利尼奥',
    u'卡瓦德蒂雷尼',
    u'卡斯特罗（莱切省）',
    u'基耶蒂',
    u'切法卢',
    u'曼弗雷多尼亚',
    u'皮恩扎',
    u'佩斯基奇',
    u'梅拉诺',
    u'翡翠海岸',
    u'菲诺港',
    u'马萨夫拉',
    u'布拉',
    u'苏黎世',
    u'琉森',
    u'伯尔尼',
    u'日内瓦',
    u'因特拉肯',
    u'洛桑',
    u'采尔马特',
    u'蒙特勒',
    u'圣莫里茨',
    u'施皮茨',
    u'沃韦',
    u'巴塞尔',
    u'沃州',
    u'瓦莱州',
    u'格劳宾登州',
    u'提契诺州',
    u'沙夫豪森',
    u'卢加诺',
    u'上瓦尔登州',
    u'劳特布龙嫩',
    u'圣加仑',
    u'英格堡',
    u'洛伊克巴德',
    u'库尔',
    u'米伦',
    u'洛迦诺',
    u'达沃斯',
    u'施泰因',
    u'贝林佐纳',
    u'弗里堡州',
    u'图恩',
    u'格吕耶尔',
    u'锡永',
    u'迈林根',
    u'龙疆',
    u'阿尔高州',
    u'贝特默阿尔卑',
    u'尼永',
    u'坎德斯泰格',
    u'纳沙泰尔',
    u'弗里堡',
    u'巴塞尔乡村州',
    u'莱克斯',
    u'布里恩茨',
    u'基佩尔',
    u'马焦雷湖',
    u'莫尔日',
    u'汝拉州',
    u'安德马特',
    u'伦策海德',
    u'布里格',
    u'马蒂尼',
    u'罗曼莫蒂耶',
    u'图尔高州',
    u'下瓦尔登州',
    u'科佩',
    u'外阿彭策尔州',
    u'格拉鲁斯州',
    u'内阿彭策尔州',
    u'埃默河谷',
    u'穆尔根塔尔',
    u'欧博纳',
    u'莱伯恩山',
]

batch2 = [
    u'伦敦',
    u'爱丁堡',
    u'剑桥',
    u'曼彻斯特',
    u'牛津',
    u'巴斯',
    u'伯明翰',
    u'约克',
    u'利物浦',
    u'英国湖区',
    u'苏格兰',
    u'格拉斯哥',
    u'约克郡',
    u'苏格兰高地',
    u'萨默塞特',
    u'因佛内斯',
    u'北爱尔兰',
    u'贝尔法斯特',
    u'威尔特郡',
    u'温德米尔',
    u'威尔士',
    u'天空岛',
    u'东萨塞克斯',
    u'德文郡',
    u'多塞特郡',
    u'埃塞克斯郡',
    u'萨里',
    u'阿伯丁',
    u'布赖顿',
    u'科茨沃尔德',
    u'西苏塞克斯',
    u'埃文河畔斯特拉特福',
    u'怀特岛',
    u'赫特福德郡',
    u'斯塔福德',
    u'伦敦德里',
    u'诺维奇',
    u'加帝夫',
    u'威廉堡',
    u'莱斯特',
    u'德里',
    u'兰迪德诺',
    u'坎特伯雷',
    u'布里斯托尔',
    u'斯旺西',
    u'埃姆斯伯里',
    u'凯西克',
    u'温彻斯特',
    u'伊普斯威奇',
    u'邓迪',
    u'诺丁汉',
    u'斯特灵',
    u'苏格兰国家公园',
    u'泽西',
    u'考文垂',
    u'多切斯特',
    u'彭赞斯',
    u'达勒姆',
    u'布拉德福德',
    u'哈罗盖特',
    u'普雷斯顿',
    u'彭布罗克郡',
    u'波伊斯',
    u'泰恩河畔纽卡斯尔',
    u'伊斯特本',
    u'科尔切斯特',
    u'舒兹伯利',
    u'利兹',
    u'艾尔',
    u'伯恩矛斯',
    u'切斯特',
    u'根西岛',
    u'布什米尔斯',
    u'卡莱尔',
    u'沃灵顿',
    u'伍斯特',
    u'阿尼克',
    u'阿马',
    u'切斯特菲尔德',
    u'设得兰群岛',
    u'斯托克波特',
    u'北安普敦',
    u'圣安德鲁斯',
    u'罗亚尔坦布里奇韦尔斯',
    u'米德尔斯堡',
    u'梅德斯通',
    u'纽伯里',
    u'布莱克浦',
    u'特尔福德',
    u'波顿',
    u'圣艾夫斯',
    u'肯德尔',
    u'马恩岛',
    u'史诺多尼亚国家公园',
    u'塞文欧克斯',
    u'直布罗陀',
    u'达林顿',
    u'斯温顿',
    u'卡里克弗格斯',
    u'哈德斯菲尔德',
    u'伍尔弗汉普顿',
    u'Ashford',
    u'彼得伯勒',
    u'汤顿',
    u'法纳姆',
    u'巴恩斯利',
    u'班戈',
    u'沃特福德',
    u'贝里圣埃德蒙兹',
    u'赫克瑟姆',
    u'勒威克',
    u'廷塔杰尔',
    u'伯恩利',
    u'海威科姆',
    u'约克郡谷地',
    u'维甘',
    u'米尔顿凯因斯',
    u'皮特洛赫里',
    u'南安普敦',
    u'卡菲利',
    u'谢菲尔德',
    u'尼斯湖',
    u'康维',
    u'埃尔金',
    u'安布赛德',
    u'赛伦塞斯特',
    u'峰区',
    u'卡纳芬',
    u'格洛斯特',
    u'阿维莫',
    u'贝辛斯托克',
    u'埃克斯穆尔国家公园',
    u'沃里克',
    u'托基',
    u'查尔顿汉姆',
    u'杰德堡',
    u'霍沃思',
    u'奇平卡姆登',
    u'赫默尔亨普斯特德',
    u'赫尔',
    u'道格拉斯',
    u'福克斯通',
    u'兰戈伦',
    u'彭里斯',
    u'绍斯波特',
    u'布雷肯比肯斯国家公园',
    u'马盖特',
    u'拉姆斯盖特',
    u'巴林托伊',
    u'诺森伯兰国家公园',
    u'皇家利明顿矿泉市',
    u'雷克斯汉姆',
    u'奥克汉普顿',
    u'克罗伊登',
    u'艾尔斯伯里',
    u'沃金厄姆',
    u'贝克韦尔',
    u'利明顿',
    u'查塔姆',
    u'霍克斯黑德',
    u'北贝里克',
    u'格伦里丁',
    u'古罗克',
    u'皮布尔斯',
    u'阿伯里斯特威斯',
    u'斯特拉特福德',
    u'格拉斯米尔湖',
    u'艾伦岛',
    u'帕尔',
    u'拉格伦',
    u'卡斯特',
    u'比克雷',
    u'雅典',
    u'圣托里尼',
    u'基克拉泽斯群岛',
    u'米科诺斯岛',
    u'伯罗奔尼撒',
    u'提洛斯岛',
    u'萨罗尼科斯群岛',
    u'蒂诺斯岛',
    u'克里特岛',
    u'多德卡尼斯群岛',
    u'罗德岛',
    u'萨罗尼加',
    u'科孚岛',
    u'扎金索斯',
    u'纳夫普利翁',
    u'纳克索斯',
    u'梅黛奥拉',
    u'干尼亚',
    u'斯波拉泽斯群岛',
    u'伊拉克利翁',
    u'斯基亚索斯岛',
    u'帕罗斯岛',
    u'希俄斯岛',
    u'雷西姆农',
    u'德尔菲',
    u'科斯岛',
    u'米洛斯岛',
    u'斯科派洛斯岛',
    u'卡兰巴卡',
    u'伊亚',
    u'莱夫卡扎',
    u'拉里萨',
    u'帕特雷',
    u'阿莫尔戈斯岛',
    u'迈锡尼',
    u'科莫蒂尼',
    u'伊奥斯',
    u'卡尔帕索斯',
    u'亚里山德鲁波利斯',
    u'莱斯博斯岛',
    u'耶拉派特拉',
    u'安德罗斯岛',
    u'萨摩斯岛',
    u'萨索斯岛',
    u'圣尼古拉奥斯',
    u'沃洛斯',
    u'卡瓦拉',
    u'萨米',
    u'马塔拉',
    u'比雷欧斯',
    u'福莱甘兹罗斯岛',
    u'斯巴达',
    u'科斯镇',
    u'埃皮扎夫罗斯',
    u'帕罗奇亚',
    u'纳夫帕克托斯',
    u'科林斯',
    u'基斯诺斯岛',
    u'阿拉霍瓦',
    u'拉米亚',
    u'阿尔戈斯托利翁',
    u'佩弗奇',
    u'优卑亚岛',
    u'卡林诺斯岛',
    u'帕特莫斯',
    u'普雷韦扎',
    u'苏尼翁',
    u'波罗斯岛',
    u'米蒂利尼',
    u'马拉松',
    u'莫奈姆瓦夏',
    u'韦瑞洛纳',
    u'锡罗斯岛',
    u'斯塔罗斯',
    u'卡拉马孔',
    u'卡尔派尼西翁',
    u'基西拉岛',
    u'波多河丽',
    u'阿基阿婆斯托里',
    u'伊西翁',
    u'伊萨卡岛',
    u'圣斯特凡诺斯',
    u'瑙萨玛西亚斯',
    u'皮尔戈斯',
    u'天堂海滩',
    u'塞尔米',
    u'马蒂',
    u'韦里亚',
    u'阿纳菲岛',
    u'拉斐那',
    u'伊古迈尼察',
    u'Agios Konstantinos',
    u'卡摩雷斯',
    u'瓦尔基扎',
    u'伊德拉岛',
    u'纳乌萨',
    u'皮索·里瓦蒂',
    u'阿柴格罗斯',
    u'格雷韦纳',
    u'奥诺斯',
    u'德里奥斯',
    u'阿尔戈斯',
    u'奥雷斯蒂阿斯',
    u'莱罗斯岛',
    u'斯塔夫罗斯',
    u'帕瑞加',
    u'特里卡拉',
    u'扎哈罗',
    u'埃尔莫波利斯',
    u'图罗斯',
    u'特力安塔',
    u'帕诺尔莫斯',
    u'奥林匹亚',
    u'新马克立',
    u'特里波利斯',
    u'埃雷特里亚',
    u'迈索隆吉翁',
    u'佩雷亚',
    u'卡马利',
    u'费拉',
    u'梅加洛克豪略翁',
    u'乔拉',
    u'依克希亚',
    u'萨索斯',
    u'伊卡利亚岛',
    u'卡达麦纳',
    u'新安希亚洛斯',
    u'卡拉马塔',
    u'柏林',
    u'慕尼黑',
    u'法兰克福',
    u'汉堡',
    u'海德堡',
    u'科隆',
    u'福森',
    u'巴伐利亚',
    u'巴登-符腾堡州',
    u'黑森州',
    u'纽伦堡',
    u'罗滕堡',
    u'北莱茵-威斯特法伦',
    u'维尔茨堡',
    u'斯图加特',
    u'莱茵兰-普法尔茨',
    u'浪漫之路',
    u'萨克森',
    u'德累斯顿',
    u'杜塞尔多夫',
    u'黑森林',
    u'贝希特斯加登',
    u'科布伦茨',
    u'勃兰登堡',
    u'波恩',
    u'下萨克森',
    u'汉诺威',
    u'美因茨',
    u'石勒苏益格-荷尔斯泰因',
    u'奥格斯堡',
    u'霍恩施万高',
    u'梅克伦堡-前波莫瑞',
    u'图林根',
    u'巴登巴登',
    u'萨克森-安哈尔特',
    u'波茨坦',
    u'莱比锡',
    u'班堡',
    u'不莱梅',
    u'特里尔',
    u'雷根斯堡',
    u'多特蒙德',
    u'威斯巴登',
    u'吕贝克',
    u'埃森',
    u'乌尔姆',
    u'康斯坦茨',
    u'亚琛',
    u'加尔米施-帕滕基兴',
    u'罗斯托克',
    u'曼海姆',
    u'帕绍',
    u'艾福特',
    u'佛莱堡',
    u'博登湖',
    u'马格德堡',
    u'拜罗伊特',
    u'魏玛',
    u'不伦瑞克',
    u'萨尔兰',
    u'卡塞尔',
    u'蒂宾根',
    u'吕根岛',
    u'什未林',
    u'基尔',
    u'哈雷',
    u'沃尔夫斯堡',
    u'莱茵河畔吕德斯海姆',
    u'讷德林根',
    u'英戈尔施塔特',
    u'杜伊斯堡',
    u'耶拿',
    u'波鸿',
    u'科黑姆',
    u'卡尔斯鲁厄',
    u'萨尔布吕肯',
    u'丁克尔斯比尔',
    u'富尔达',
    u'施派尔',
    u'施韦比施哈尔',
    u'伍珀塔尔',
    u'格丁根',
    u'科堡',
    u'帕德博恩',
    u'哈瑙',
    u'叙尔特岛',
    u'韦尔特海姆',
    u'林道',
    u'奎德林堡',
    u'施特拉尔松德',
    u'盖尔森基兴',
    u'希尔德斯海姆',
    u'茨维考',
    u'鲍岑',
    u'辛根',
    u'路德城维滕贝格',
    u'德绍',
    u'奥斯纳布吕克',
    u'戈斯拉尔',
    u'弗伦斯堡',
    u'迈森',
    u'巴哈拉',
    u'滴滴湖',
    u'海尔布隆',
    u'博帕尔德',
    u'维斯马',
    u'布吕尔',
    u'特里贝格',
    u'圣戈阿尔',
    u'施韦因富特',
    u'勒沃库森',
    u'卡尔夫',
    u'巴林根',
    u'门兴格拉德巴赫',
    u'艾森纳赫',
    u'路德维希堡',
    u'哈默尔恩',
    u'锡根',
    u'弗罗伊登施塔特',
    u'布尔格',
    u'罗拉赫',
    u'施泰因加登',
    u'富特旺根',
    u'多瑙艾辛根',
    u'根根堡',
    u'安德希斯',
    u'圣戈阿尔斯豪森',
    u'亚格斯特采尔',
    u'萨航',
    u'豪斯哈姆',
    u'米特巴赫',
    u'伊斯坦布尔',
    u'伊兹密尔',
    u'卡帕多奇亚',
    u'棉花堡',
    u'格雷梅',
    u'安塔利亚',
    u'萨夫兰博卢（番红花城）',
    u'费特希耶',
    u'安卡拉',
    u'塞尔丘克',
    u'恰纳卡莱',
    u'库萨达斯',
    u'博德鲁姆',
    u'孔亚',
    u'代尼兹利',
    u'以弗所',
    u'特拉布宗省',
    u'阿兰亚',
    u'加利波利半岛',
    u'特拉布宗',
    u'席里恩斯',
    u'埃迪尔内',
    u'迪亚巴克尔',
    u'梅尔辛',
    u'阿达纳',
    u'马米勒斯',
    u'阿马西亚',
    u'加济安泰普',
    u'埃斯基谢希尔',
    u'切什梅',
    u'马尔丁',
    u'格克切岛',
    u'卡什',
    u'尚勒乌尔法',
    u'西戴',
    u'贝尔加马',
    u'穆拉',
    u'埃尔祖鲁姆',
    u'安塔基亚',
    u'凡城',
    u'内夫谢希尔',
    u'开赛利',
    u'于尔居普',
    u'博卢省',
    u'锡瓦斯',
    u'开尔斯',
    u'多乌巴亚泽特',
    u'阿瓦诺斯',
    u'奥尔杜',
    u'阿克萨赖',
]

batch3 = [
    u'巴塞罗那',
    u'马德里',
    u'瓦伦西亚',
    u'塞维利亚',
    u'格拉纳达',
    u'托莱多',
    u'龙达',
    u'塞哥维亚',
    u'科尔多瓦',
    u'马拉加',
    u'萨拉曼卡',
    u'萨拉戈萨',
    u'毕尔巴鄂',
    u'锡切斯',
    u'阿维拉',
    u'马略卡岛',
    u'加的斯',
    u'阿利坎特',
    u'圣地亚哥-德孔波斯特拉',
    u'赫罗纳',
    u'塔拉戈纳',
    u'阿尔卡拉·德·埃纳雷斯',
    u'加那利群岛',
    u'伊维萨岛',
    u'巴利阿里群岛',
    u'马贝拉',
    u'特内里费',
    u'昆卡',
    u'桑坦德',
    u'潘普洛纳',
    u'塔里法',
    u'米哈斯',
    u'莱昂',
    u'布尔戈斯',
    u'梅里达',
    u'穆尔西亚',
    u'奥维耶多',
    u'内尔哈',
    u'赫雷斯-德拉弗龙特拉',
    u'巴利亚多利德',
    u'菲格拉斯',
    u'卡塞雷斯',
    u'安达卢西亚',
    u'拉曼恰',
    u'阿拉贡',
    u'加利西亚',
    u'巴斯克',
    u'埃斯特雷马杜拉',
    u'兰沙略得',
    u'坎塔布里亚',
    u'阿斯图里亚斯',
    u'大加那利岛',
    u'纳瓦拉',
    u'罗列特海岸',
    u'拉科鲁利亚',
    u'托雷莫里斯',
    u'拉里奥哈',
    u'梅诺卡岛',
    u'阿兰胡埃斯',
    u'圣塞瓦斯蒂安',
    u'富埃特文图拉岛',
    u'哈恩',
    u'洛格罗尼奥',
    u'阿拉瓦省',
    u'韦尔瓦',
    u'托雷维耶哈',
    u'贝尼东',
    u'维多利亚',
    u'索里亚',
    u'滨海托萨',
    u'乌韦达',
    u'拉斯帕尔马斯',
    u'巴达霍斯',
    u'芬吉萝拉',
    u'埃尔切',
    u'戈梅拉岛',
    u'福门特拉岛',
    u'塔拉萨',
    u'哈韦阿',
    u'德尼亚',
    u'特内利费-圣克鲁斯',
    u'比戈',
    u'拉帕尔马',
    u'萨洛',
    u'卡斯特利翁-德拉普拉纳',
    u'卡尔佩',
    u'休达',
    u'弗里希利亚纳',
    u'特鲁埃尔',
    u'阿尔科伊',
    u'莱里达省',
    u'坎加斯-德奥尼斯',
    u'甘迪亚',
    u'费罗尔',
    u'卢戈省',
    u'莱里达',
    u'赫塔费',
    u'阿尔科尔孔',
    u'瓜代拉堡',
    u'阿尔梅里亚',
    u'阿尔赫西拉斯',
    u'贝尼卡西姆',
    u'萨莫拉',
    u'里波尔',
    u'艾朗',
    u'奇皮奥纳',
    u'阿拉塞纳',
    u'钦琼',
    u'潘蒂科萨',
    u'利亚戈斯特拉',
    u'梅利利亚',
    u'埃尔·埃斯科里亚尔',
    u'莫斯科',
    u'圣彼得堡',
    u'海参崴',
    u'伊尔库茨克',
    u'苏兹达尔',
    u'弗拉基米尔',
    u'西伯利亚联邦管区',
    u'索契',
    u'新西伯利亚州',
    u'雅罗斯拉夫尔',
    u'喀山',
    u'克拉斯诺达尔',
    u'下诺夫哥罗德州',
    u'新西伯利亚',
    u'萨马拉',
    u'乌法',
    u'车里雅宾斯克',
    u'伏尔加格勒',
    u'鄂木斯克',
    u'克拉斯诺雅尔斯克',
    u'科斯特罗马',
    u'巴尔瑙尔',
    u'托木斯克',
    u'沃罗涅日',
    u'阿尔汉格尔斯克',
    u'大诺夫哥罗德',
    u'梁赞',
    u'沃洛格达',
    u'普斯科夫',
    u'哈巴罗夫斯克',
    u'阿斯特拉罕',
    u'摩尔曼斯克',
    u'库尔斯克',
    u'雅库茨克',
    u'乌兰乌德',
    u'萨拉托夫',
    u'新库兹涅茨克',
    u'阿巴坎',
    u'谢尔盖耶夫镇',
    u'别尔哥罗德',
    u'乌格里奇',
    u'佩列斯拉夫尔-扎列斯基',
    u'叶卡捷琳堡',
    u'库尔干',
    u'新罗西斯克',
    u'加里宁格勒',
    u'顿河畔罗斯托夫',
    u'布拉戈维申斯克',
    u'托博尔斯克',
    u'阿穆尔河畔共青城',
    u'皮亚季戈尔斯克',
    u'弗拉季高加索',
    u'旧鲁萨',
    u'彼尔姆',
    u'彼得罗扎沃茨克',
    u'利斯特维扬卡',
    u'奥尔洪',
    u'维堡',
    u'斯摩棱斯克',
    u'秋明',
    u'普乔雷',
    u'贝加尔湖',
    u'贝加尔斯克',
    u'赤塔',
    u'格罗兹尼',
    u'南萨哈林斯克',
    u'普廖斯',
    u'堪察加彼得罗巴甫洛夫斯克',
    u'索洛韦茨基群岛',
    u'斯拉维扬卡',
    u'马哈奇卡拉',
    u'阿尔乔姆',
    u'比斯克',
    u'埃利斯塔',
    u'斯柳江卡',
    u'阿姆斯特丹',
    u'鹿特丹',
    u'海牙',
    u'代尔夫特',
    u'马斯特里赫特',
    u'乌特勒支',
    u'莱顿',
    u'埃因霍温',
    u'格罗宁根',
    u'哈勒姆',
    u'吕伐登',
    u'豪达',
    u'阿尔克马尔',
    u'布雷达',
    u'兹沃勒',
    u'希特霍伦',
    u'阿纳姆',
    u'斯海尔托亨博斯',
    u'泰瑟尔岛',
    u'奈梅亨',
    u'沃伦丹',
    u'阿珀尔多伦',
    u'恩斯赫德',
    u'霍伦',
    u'多德雷赫特',
    u'登海尔德',
    u'艾登',
    u'马肯',
    u'Bergen op Zoom',
    u'海斯特伦',
    u'维也纳',
    u'萨尔茨堡',
    u'哈尔施塔特',
    u'因斯布鲁克',
    u'格拉茨',
    u'奥地利阿尔卑斯山',
    u'卡林西亚',
    u'梅尔克',
    u'林茨',
    u'克拉根福',
    u'巴德依舍',
    u'圣沃夫冈',
    u'布雷根茨',
    u'格蒙登',
    u'多瑙河畔克雷姆斯',
    u'施泰尔',
    u'艾森斯塔特',
    u'圣吉尔根',
    u'菲拉赫',
    u'利恩茨',
    u'穆劳',
    u'哈莱因',
    u'克洛斯特新堡',
    u'施瓦茨',
    u'萨尔茨卡默古特',
    u'韦尔芬',
    u'费尔德基希',
    u'上特劳恩',
    u'库夫施坦',
    u'鲁斯特',
    u'玛丽亚采尔',
    u'布卢登茨',
    u'穆尔河畔布鲁克',
    u'蒙德湖',
    u'布拉格',
    u'克鲁姆洛夫',
    u'卡罗维发利',
    u'皮尔森',
    u'库特纳霍拉',
    u'捷克布杰约维采',
    u'布尔诺',
    u'奥洛穆茨',
    u'利托米什尔',
    u'玛丽亚温泉市',
    u'俄斯特拉发',
    u'泰尔奇',
    u'卡罗维发利州',
    u'塔博尔',
    u'里斯本',
    u'波尔图',
    u'辛特拉',
    u'马德拉群岛',
    u'卡斯凯斯',
    u'马德拉',
    u'埃武拉',
    u'丰沙尔',
    u'法鲁',
    u'拉古什',
    u'科英布拉',
    u'亚速尔群岛',
    u'阿尔布费拉',
    u'阿威罗',
    u'布拉加',
    u'奥比都斯',
    u'维拉摩拉',
    u'阿尔科巴萨',
    u'巴塔利亚',
    u'蓬塔德尔加达',
    u'波尔蒂芒',
    u'塔维拉',
    u'维亚纳堡',
    u'萨格里什',
    u'塞图巴尔',
    u'桑塔岛',
    u'锡尔维什',
    u'托马尔',
    u'布鲁塞尔',
    u'布鲁日',
    u'安特卫普',
    u'根特',
    u'鲁汶',
    u'奥斯坦德',
    u'法兰德斯',
    u'图尔奈',
    u'纳慕尔',
    u'哈瑟尔特',
    u'列日',
    u'伊普尔',
    u'奥斯陆',
    u'卑尔根',
    u'斯塔万格',
    u'特隆赫姆',
    u'特罗姆瑟',
    u'莫尔德',
    u'克里斯蒂安桑',
    u'博德',
    u'克里斯蒂安松',
    u'阿雷松德',
    u'弗莱姆',
    u'哈尔斯塔',
    u'罗弗敦群岛',
    u'朗伊尔城',
    u'奥达',
    u'纳尔维克',
    u'洛姆',
    u'盖朗格',
    u'安德内斯',
    u'翁达尔斯内斯',
    u'卡拉绍克',
    u'德拉门',
    u'利勒哈默尔',
    u'埃德菲尤尔',
    u'巴勒斯特兰',
    u'拉尔维克',
    u'希尔科内斯',
    u'哈尔登',
    u'哈默弗斯特',
    u'腓特烈斯塔',
    u'松达尔',
    u'米达尔',
    u'孔斯贝格',
    u'斯特林',
    u'希恩',
    u'苏特兰',
    u'穆村',
    u'耶卢',
    u'哈马尔',
    u'居德旺恩',
    u'艾于兰',
    u'海于格松',
    u'巴伦支堡',
    u'赫尔辛基',
    u'罗瓦涅米',
    u'坦佩雷',
    u'埃斯波',
    u'库奥皮奥',
    u'图尔库',
    u'奥卢',
    u'拉彭兰塔',
    u'拉赫蒂',
    u'凯米',
    u'科科拉',
    u'劳马',
    u'科特卡',
    u'海门林纳',
    u'楠塔利',
    u'基尔皮斯耶尔维',
    u'萨翁林纳',
    u'伊马特拉',
    u'库萨莫',
    u'瓦萨',
    u'卡亚尼',
    u'托尔尼奥',
    u'玛丽港',
    u'约恩苏',
    u'伊瓦洛',
    u'基蒂莱',
    u'伊纳里',
    u'哈米纳',
    u'汉科',
    u'苏丹屈莱',
    u'库姆灵厄',
    u'塔瓦斯比',
    u'Saarenkylä',
    u'布达佩斯',
    u'巴拉顿湖区',
    u'圣安德烈',
    u'赛格德',
    u'埃格尔',
    u'德布勒森',
    u'杰尔',
    u'米什科尔茨',
    u'凯斯特海伊',
    u'肖普朗',
    u'维谢格拉德',
    u'埃斯泰尔戈姆',
    u'Kecskemet',
    u'帝豪尼',
    u'格德勒',
    u'斯德哥尔摩',
    u'哥德堡',
    u'马尔默',
    u'赫尔辛堡',
    u'阿比斯库',
    u'乌普萨拉',
    u'斯科讷',
    u'隆德',
    u'韦司特洛斯',
    u'哥得兰岛',
    u'基律纳',
    u'林雪平',
    u'厄勒布鲁',
    u'于默奥',
    u'诺尔雪平',
    u'卡尔斯克鲁纳',
    u'法伦',
    u'瓦斯泰纳',
    u'卡尔斯塔德',
    u'约克莫克',
    u'卡尔马',
    u'厄斯特松德',
    u'松兹瓦尔',
    u'哥本哈根',
    u'腓特烈港',
    u'锡尔克堡',
    u'博恩霍尔姆岛',
    u'埃斯比约',
    u'赫尔辛格',
    u'欧登塞',
    u'斯卡恩',
    u'奥胡斯',
    u'罗斯基勒',
    u'科灵',
    u'奥尔堡',
    u'凯隆堡',
    u'里伯',
    u'朗厄兰岛',
    u'法尔斯特岛',
    u'埃伯尔措夫特',
    u'希勒勒',
    u'斯文堡',
    u'比隆',
    u'希茨海尔斯',
    u'洛兰岛',
    u'默恩岛',
    u'克厄',
]

batch4 = [
    u'雷克雅未克',
    u'阿克雷里',
    u'维克',
    u'冰岛东部区',
    u'米湖',
    u'冰岛南部区',
    u'胡萨维克',
    u'埃伊尔斯塔奇',
    u'韦斯特曼纳埃亚尔',
    u'华姆斯唐吉',
    u'绿森堡市',
    u'华沙',
    u'克拉科夫',
    u'格但斯克',
    u'波兰中郡',
    u'波罗的海沿岸',
    u'比得哥什',
    u'波兹南',
    u'扎科帕内',
    u'什切青',
    u'格丁尼亚',
    u'卢布林',
    u'卡托维兹',
    u'罗兹',
    u'托伦',
    u'索波特',
    u'弗罗茨瓦夫',
    u'琴斯托霍瓦',
    u'奥博蕾',
    u'卡尔帕奇',
    u'皮瓦',
    u'都柏林',
    u'基拉尼',
    u'科克',
    u'高威',
    u'垂利',
    u'金赛尔',
    u'沃特福德',
    u'基尔代尔郡',
    u'巴利香农',
    u'恩尼斯',
    u'阿斯隆',
    u'丁格尔',
    u'基尔肯尼',
    u'威克洛',
    u'布瑞',
    u'康尼玛拉',
    u'基尔基尔',
    u'马拉海德',
    u'阿克洛',
    u'蒙特卡洛',
    u'摩纳哥城',
    u'斯普利特',
    u'杜布罗夫尼克',
    u'萨格勒布',
    u'罗维尼',
    u'扎达尔',
    u'希贝尼克',
    u'里耶卡',
    u'特罗吉尔',
    u'波雷奇',
    u'奥帕蒂亚',
    u'普利特维采湖群国家公园',
    u'科尔丘拉岛',
    u'赫瓦尔',
    u'茨雷斯岛',
    u'维斯',
    u'布拉迪斯拉发',
    u'班斯卡·比斯特里察',
    u'普雷绍夫州',
    u'波普拉德',
    u'特尔纳瓦州',
    u'斯皮什斯凯波德赫拉杰',
    u'塔林',
    u'答尔丢夫',
    u'帕尔努',
    u'拉克韦雷',
    u'布加勒斯特',
    u'锡比乌',
    u'布拉索夫',
    u'雅西',
    u'拉迪亚',
    u'苏恰瓦',
    u'克鲁拿波卡',
    u'蒂米什瓦拉',
    u'斯哥莎拉',
    u'图尔恰',
    u'希奈亚',
    u'亚拉得',
    u'卢布尔雅那',
    u'马里博尔',
    u'皮兰',
    u'布莱德',
    u'克拉尼斯卡戈拉',
    u'科佩尔',
    u'拉多夫利察',
    u'波斯托伊纳',
    u'利马索尔',
    u'帕福斯',
    u'尼科西亚',
    u'阿伊亚纳帕',
    u'拉纳卡',
    u'凯里尼亚',
    u'特罗多斯山',
    u'法马古斯塔',
    u'卡科佩特里亚',
    u'索非亚',
    u'瓦尔纳州',
    u'瓦尔纳',
    u'普罗夫迪夫',
    u'索佐波尔',
    u'班斯科',
    u'大特尔诺沃州',
    u'希普卡',
    u'科普里夫什蒂察',
    u'梅尔尼克',
    u'维尔纽斯县',
    u'考纳斯县',
    u'希奥利艾县',
    u'克莱佩达',
    u'帕兰加',
    u'特拉凯',
    u'基辅',
    u'波尔塔瓦',
    u'切尔诺夫策',
    u'利沃夫',
    u'Crimean Peninsula',
    u'哈尔科夫',
    u'切尔尼戈夫',
    u'乌日霍罗德',
    u'日托米尔',
    u'顿涅茨克',
    u'塞瓦斯托波尔',
    u'扎波罗热',
    u'敖德萨',
    u'雅尔塔',
    u'巴赫奇萨赖',
    u'贝尔格莱德',
    u'里加',
    u'尤尔马拉',
    u'锡古尔达',
    u'文茨皮尔斯',
    u'陶格夫匹尔斯',
    u'马耳他岛',
    u'瓦莱塔',
    u'马利哈',
    u'斯利马',
    u'戈佐岛',
    u'圣朱利安',
    u'圣保罗湾',
    u'科米诺岛',
    u'瓦杜兹',
    u'明斯克',
    u'维帖布斯克',
    u'格罗德诺',
    u'布列斯特',
    u'波洛茨克',
    u'科托尔',
    u'波德戈里察',
    u'杜米托尔国家公园',
    u'采蒂涅',
    u'扎布利亚克',
    u'赫尔采格诺维',
    u'蒂瓦特',
    u'布德瓦',
    u'第比利斯',
    u'巴统',
    u'库塔伊西',
    u'西格纳吉',
    u'斯特潘茨明达',
    u'泰拉维',
    u'梅斯蒂亚',
    u'阿哈尔齐赫',
    u'祖格迪迪',
    u'姆茨赫塔',
    u'埃里温',
    u'迪利然',
    u'阿拉韦尔迪',
    u'戈里斯',
    u'塞万',
    u'诺拉旺克',
    u'埃奇米亚津',
    u'安道尔城',
    u'地拉那',
    u'吉诺卡斯特',
    u'培拉特',
    u'斯科普里',
    u'奥赫里德',
    u'莫斯塔尔',
    u'萨拉热窝',
    u'亚伊采',
    u'托尔斯',
    u'卡拉卡斯维克',
    u'基希讷乌',
    u'新布尔多',
    u'乌罗舍瓦茨',
    u'塞拉瓦莱',
    u'阿夸维瓦',
    u'博尔戈·马吉欧雷',
    u'基埃萨努欧瓦',
    u'多玛尼亚诺',
    u'法尔齐亚诺',
    u'科里阿尼诺',
    u'蒙泰吉阿迪诺',
    u'圣马力诺',
]
