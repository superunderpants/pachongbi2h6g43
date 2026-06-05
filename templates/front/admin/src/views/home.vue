<template>
	<div class="home-content" :style="{'backgroundImage': indexBgUrl?`url(${$base.url + indexBgUrl})`:''}">
		<!-- title -->
		<div id="home-title" class="home-title animate__animated">
			<div class="titles" >
				<span>欢迎使用</span>
				{{this.$project.projectName}}
			</div>
		</div>
		<!-- statis -->
		<div class="statis-box">
			<div id="statis1" class="statis1 animate__animated" v-if="isAuth('autohome','首页总数')">
				<div class="left">
					<span class="icon iconfont icon-liulan12"></span>
				</div>
				<div class="right">
					<div class="num">{{autohomeCount}}</div>
					<div class="name">新能源资讯总数</div>
				</div>
			</div>
			<div id="statis2" class="statis2 animate__animated" v-if="isAuth('xingyezixun','首页总数')">
				<div class="left">
					<span class="icon iconfont icon-shuju17"></span>
				</div>
				<div class="right">
					<div class="num">{{xingyezixunCount}}</div>
					<div class="name">行业资讯总数</div>
				</div>
			</div>
		</div>
		<!-- statis -->
		<div id="news-box" class="news-box animate__animated">
			<div class="news-title">
				系统公告
			</div>
			<div class="news-list">
				<div class="news-item" v-for="(item,index) in newsList" :index="index" @click="newsDetailClick(item)">
					<div class="news-text">
						{{item.title}}
					</div>
					<div class="news-img-box">
						<img :src="item.picture?($base.url + item.picture.split(',')[0]):''" alt="">
					</div>
					<div class="news-desc">
						{{item.introduction}}
					</div>
					<div class="news-time">
						{{item.addtime}}
					</div>
				</div>
			</div>
		</div>
		<el-dialog :visible.sync="newsVisible" title="系统公告" :append-to-body="true" width="60%">
			<div style="width: 100%;text-align: center;font-size: 20px;color: #000;padding: 0 0 20px;font-weight: bold;">{{newsDetail.title}}</div>
			<div style="width: 100%;">
				<div class="ql-snow ql-editor" v-html="newsDetail.content"></div>
			</div>
		</el-dialog>
	
		<!-- echarts -->
		<!-- 6 -->
		<div class="type6">
			<div class="echarts1 animate__animated" v-if="isAuth('autohome','首页统计',2)">
				<div id="autohomeChart1" style="width: 100%;height: 100%"></div>
			</div>
			<div class="echarts2 animate__animated" v-if="isAuth('autohome','首页统计',2)">
				<div id="autohomeChart2" style="width: 100%;height: 100%"></div>
			</div>
			<div class="echarts3 animate__animated" v-if="isAuth('xingyezixun','首页统计',2)">
				<div id="xingyezixunChart1" style="width: 100%;height: 100%"></div>
			</div>
			<div class="echarts4 animate__animated" v-if="isAuth('xingyezixun','首页统计',2)">
				<div id="xingyezixunChart2" style="width: 100%;height: 100%"></div>
			</div>
			<div class="echarts5 animate__animated" v-if="isAuth('xingyezixun','首页统计',2)">
				<div id="xingyezixunChart3" style="width: 100%;height: 100%"></div>
			</div>
			<div class="echarts6 animate__animated" v-if="isAuth('xingyezixun','首页统计',2)">
				<el-select
					v-if="changeStatQuery(['users'])"
					v-model="xingyezixunchartQuery4.faburen" placeholder="发布人" @change="xingyezixunChat4" clearable>
					<el-option v-for="item in xingyezixunChartOptions4" :label="item" :value="item"></el-option>
				</el-select>
				<div id="xingyezixunChart4" style="width: 100%;height: 100%"></div>
			</div>
		</div>
		<!-- echarts -->
	</div>
</template>
<script>
import 'animate.css'
//6
import router from '@/router/router-static'
import * as echarts from 'echarts'
export default {
	data() {
		return {
			autohomeCount: 0,
			xingyezixunCount: 0,
			xingyezixunchartQuery4: {},
			xingyezixunChartOptions4: [],
			line: {"backgroundColor":"transparent","yAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":15,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#00AB6D","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#00AB6D","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#00AB6D","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"minInterval":1,"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#00AB6D","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,0.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"xAxis":{"axisLabel":{"borderType":"solid","rotate":30,"padding":0,"shadowOffsetX":0,"margin":10,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#00AB6D","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"truncate","borderRadius":0,"borderWidth":0,"width":120,"interval":0,"fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#00AB6D","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#00AB6D","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#00AB6D","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"color":["#4f7df5","#6ad2ff","#89e6d8","#012baf","#73c0de","#3ba272","#4495ac","#9a60b4","#ea7ccc"],"legend":{"padding":0,"itemGap":10,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"orient":"horizontal","shadowBlur":0,"bottom":"auto","itemHeight":14,"show":true,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"right":"auto","top":"auto","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"right","borderWidth":0,"width":"80%","itemWidth":20,"textStyle":{"textBorderWidth":0,"color":"inherit","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"series":{"showSymbol":true,"symbol":"emptyCircle","symbolSize":4},"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"title":{"borderType":"solid","padding":0,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"shadowBlur":0,"bottom":"auto","show":true,"right":"auto","top":"auto","borderRadius":0,"left":"left","borderWidth":0,"textStyle":{"textBorderWidth":0,"color":"#00AB6D","textShadowColor":"transparent","fontSize":14,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":600,"textBorderColor":"#666","textShadowBlur":0},"shadowColor":"transparent"}},
			bar: {"backgroundColor":"transparent","yAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":12,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"color":"#00AB6D","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#00AB6D","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#00AB6D","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"minInterval":1,"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#00AB6D","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,0.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"xAxis":{"axisLabel":{"borderType":"solid","rotate":30,"padding":0,"shadowOffsetX":0,"margin":10,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#00AB6D","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"truncate","borderRadius":0,"borderWidth":0,"width":120,"interval":0,"fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#00AB6D","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#00AB6D","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"minInterval":1,"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#00AB6D","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"color":["#00AB6D","#F0D060","#EE142F","#4B93FF","#f75d5f","#5967cc","#faa07b","#9ab7a8","#ea7ccc"],"legend":{"padding":0,"itemGap":10,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#00AB6D","shadowOffsetY":0,"orient":"horizontal","shadowBlur":0,"bottom":"auto","itemHeight":14,"show":true,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"right":"auto","top":"auto","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"right","borderWidth":0,"width":"80%","itemWidth":20,"textStyle":{"textBorderWidth":0,"color":"inherit","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":12,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"grid":{"x":"25%","y":"15%","y2":"15%","x2":"5%"},"series":{"barWidth":"12px","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"#00AB6D","shadowOffsetY":0,"color":"","shadowBlur":0,"barBorderRadius":[20,0,0,0],"borderWidth":0,"opacity":1,"shadowColor":"#00AB6D"},"colorBy":"series","barCategoryGap":"20%"},"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"title":{"borderType":"solid","padding":0,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#00AB6D","shadowOffsetY":0,"subtext":"","shadowBlur":0,"bottom":"auto","show":true,"right":"auto","subtextStyle":{"padding":[5,0,0,0],"borderColor":"red","color":"red","borderWidth":10},"top":"auto","borderRadius":0,"left":"left","borderWidth":0,"textStyle":{"textBorderWidth":0,"color":"#00AB6D","textShadowColor":"transparent","fontSize":14,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":600,"textBorderColor":"#00AB6D","textShadowBlur":0},"shadowColor":"transparent"},"base":{"animate":false,"interval":2000}},
			pie: {"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"backgroundColor":"transparent","color":["#00C07B","#baaa40","#ae3e08","#EE142F","#4B93FF","#5967cc","#faa07b","#9ab7a8","#ea7ccc"],"title":{"borderType":"solid","padding":[5,0,0,0],"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"shadowBlur":0,"bottom":"auto","show":true,"right":"auto","top":"auto","borderRadius":0,"left":"left","borderWidth":0,"textStyle":{"textBorderWidth":0,"color":"#00C07B","textShadowColor":"transparent","fontSize":14,"lineHeight":14,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":600,"textBorderColor":"#666","textShadowBlur":0},"shadowColor":"transparent"},"legend":{"padding":[5,0,0,0],"itemGap":10,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"orient":"horizontal","shadowBlur":0,"bottom":"auto","itemHeight":2,"show":true,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"right":0,"top":"auto","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"right","borderWidth":0,"width":"80%","itemWidth":2,"textStyle":{"textBorderWidth":0,"color":"inherit","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":12,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"series":{"itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"#666","shadowOffsetY":0,"color":"","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"#00C07B"},"label":{"borderType":"solid","rotate":0,"padding":0,"textBorderWidth":0,"backgroundColor":"transparent","borderColor":"#666","color":"inherit","show":true,"textShadowColor":"transparent","distanceToLabelLine":5,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"fontSize":12,"lineHeight":18,"textShadowOffsetX":0,"position":"outside","textShadowOffsetY":0,"textBorderType":"solid","textBorderColor":"#666","textShadowBlur":0},"labelLine":{"show":true,"length":10,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"#00C07B","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"#00C07B"},"length2":14,"smooth":false}}},
			funnel: {"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"backgroundColor":"transparent","color":["#00C07B","#FFEC6D","#A79100","#EE142F","#4B93FF","#5967cc","#faa07b","#9ab7a8","#ea7ccc"],"title":{"borderType":"solid","padding":2,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#ccc","shadowOffsetY":0,"shadowBlur":0,"bottom":"auto","show":true,"right":"auto","top":"auto","borderRadius":0,"left":"center","borderWidth":0,"textStyle":{"textBorderWidth":0,"color":"#03B560","textShadowColor":"transparent","fontSize":14,"lineHeight":12,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"#ccc","textShadowBlur":0},"shadowColor":"transparent"},"legend":{"padding":5,"itemGap":10,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#ccc","shadowOffsetY":0,"orient":"vertical","shadowBlur":0,"bottom":"auto","itemHeight":2,"show":true,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"top":"auto","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"left","borderWidth":0,"width":"auto","itemWidth":2,"textStyle":{"textBorderWidth":0,"color":"inherit","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":20,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"series":{"itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"#000","shadowOffsetY":0,"color":"","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"#000"},"label":{"borderType":"solid","rotate":0,"padding":0,"textBorderWidth":0,"backgroundColor":"transparent","borderColor":"#fff","color":"","show":true,"textShadowColor":"transparent","distanceToLabelLine":5,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"fontSize":12,"lineHeight":18,"textShadowOffsetX":0,"position":"outside","textShadowOffsetY":0,"textBorderType":"solid","textBorderColor":"#fff","textShadowBlur":0},"labelLine":{"show":true,"length":10,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"#000"},"length2":14,"smooth":false}}},
			boardBase: {"funnelNum":8,"lineNum":8,"radarNum":8,"gaugeNum":8,"barNum":8,"pieNum":8},
			gauge: {"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"backgroundColor":"transparent","color":["#378bb9","#095dac","#fbc62f","#16606a","#f75d5f","#5967cc","#faa07b","#9ab7a8","#ea7ccc"],"title":{"top":"top","left":"left","textStyle":{"fontSize":14,"lineHeight":24,"color":"#03B560","fontWeight":600}},"series":{"pointer":{"offsetCenter":[0,"10%"],"icon":"path://M2.9,0.7L2.9,0.7c1.4,0,2.6,1.2,2.6,2.6v115c0,1.4-1.2,2.6-2.6,2.6l0,0c-1.4,0-2.6-1.2-2.6-2.6V3.3C0.3,1.9,1.4,0.7,2.9,0.7z","width":8,"length":"80%"},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"opacity":0.5,"shadowBlur":1,"shadowColor":"#000"},"roundCap":true},"anchor":{"show":true,"itemStyle":{"color":"inherit"},"size":18,"showAbove":true},"emphasis":{"disabled":false},"progress":{"show":true,"roundCap":true,"overlap":true},"splitNumber":25,"detail":{"formatter":"{value}","backgroundColor":"inherit","color":"#fff","borderRadius":3,"width":20,"fontSize":12,"height":10},"title":{"fontSize":14},"animation":true}},
			radar: {"backgroundColor":"transparent","radar":{"shape":"circle"},"color":["#365E77","#DF308C","#0CB906","#7690cb","#49ada0","#5BBAEC","#a68a28","#EE142F","#FFE9E9"],"legend":{"padding":5,"itemGap":5,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#ccc","shadowOffsetY":0,"orient":"vertical","shadowBlur":0,"bottom":"auto","itemHeight":4,"show":true,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"right":"auto","top":"auto","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"right","borderWidth":0,"width":"auto","itemWidth":4,"textStyle":{"textBorderWidth":0,"color":"inherit","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"series":{},"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#7987FD"}},"title":{"top":"top","left":"left","textStyle":{"textBorderWidth":0,"color":"#365E77","textShadowColor":"transparent","fontSize":14,"lineHeight":14,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":600,"textBorderColor":"#666","textShadowBlur":0}}},
			newsList: [],
			newsDetail: {},
			newsVisible: false,
			indexBgUrl: '',
			indexLogoUrl: '',
		};
	},
	mounted(){
		this.init();
		this.getautohomeCount();
		if(this.isAuth('autohome','首页统计',2)){
			this.autohomeChat1();
		}
		if(this.isAuth('autohome','首页统计',2)){
			this.autohomeChat2();
		}
		this.getxingyezixunCount();
		if(this.isAuth('xingyezixun','首页统计',2)){
			this.xingyezixunChat1();
		}
		if(this.isAuth('xingyezixun','首页统计',2)){
			this.xingyezixunChat2();
		}
		if(this.isAuth('xingyezixun','首页统计',2)){
			this.xingyezixunChat3();
		}
		if(this.isAuth('xingyezixun','首页统计',2)){
			this.getxingyezixunfaburenOptions4()
			this.xingyezixunChat4();
		}
		window.addEventListener('scroll', this.handleScroll)
		setTimeout(()=>{
			this.handleScroll()
		},100)
	},
	created() {
		this.$http.get('config/info?name=bIndexBackgroundImg',).then(rs=>{this.indexBgUrl = rs.data.data?rs.data.data.value:''})
		this.$http.get('config/info?name=bHomeLogo',).then(rs=>{this.indexLogoUrl = rs.data.data?rs.data.data.value:''})
	},
	computed: {
		sessionForm() {
			return JSON.parse(this.$storage.getObj('userForm'))
		},
		avatar(){
			return this.$storage.get('headportrait')?this.$storage.get('headportrait'):''
		},
	},
	methods:{
		handleScroll() {
			let arr = [
				{id:'home-title',css:'animate__'},
				{id:'statis1',css:'animate__'},
				{id:'statis2',css:'animate__'},
				{id:'news-box',css:'animate__'},
				{id:'autohomeChart1',css:'animate__'},
				{id:'autohomeChart2',css:'animate__'},
				{id:'xingyezixunChart1',css:'animate__'},
				{id:'xingyezixunChart2',css:'animate__'},
				{id:'xingyezixunChart3',css:'animate__'},
				{id:'xingyezixunChart4',css:'animate__'},
			]
			
			for (let i in arr) {
				let doc = document.getElementById(arr[i].id)
				if (doc) {
					let top = doc.offsetTop
					let win_top = window.innerHeight + window.pageYOffset
					// console.log(top,win_top)
					if (win_top > top && doc.classList.value.indexOf(arr[i].css) < 0) {
						// console.log(doc)
						doc.classList.add(arr[i].css)
					}
				}
			}
		},
		// 统计图动画
		myChartInterval(type, xAxisData, seriesData, myChart) {
			this.$nextTick(() => {
				setInterval(() => {
					let xAxis = xAxisData.shift()
					xAxisData.push(xAxis)
					let series = seriesData.shift()
					seriesData.push(series)
				
					if (type == 1) {
						myChart.setOption({
							xAxis: [{
								data: xAxisData
							}],
							series: [{
								data: seriesData
							}]
						});
					}
					if (type == 2) {
						myChart.setOption({
							yAxis: [{
								data: xAxisData
							}],
							series: [{
								data: seriesData
							}]
						});
					}
				}, $template2.back.board.bar.base.interval);
			})
		},
		changeStatQuery(arr) {
			if(arr.length==1) {
				if(arr[0] == 'users'&&this.$storage.get("sessionTable")=='users') {
					return true
				}
			}
			let role = this.$storage.get('role')
			for(let x in arr) {
				if(arr[x] == role) {
					return true
				}
			}
			return false
		},
		init(){
			if(this.$storage.get('Token')){
				this.$http({
					url: `${this.$storage.get('sessionTable')}/session`,
					method: "get"
				}).then(({ data }) => {
					if (data && data.code != 0) {
						router.push({ name: 'login' })
					}
				});
			}else{
				router.push({ name: 'login' })
			}
			this.getNewsList()
		},
		getNewsList(){
			let params = {
				page: 1,
				limit: 7,
				sort: 'addtime',
				order: 'desc',
			}
			this.$http({
				url: `news/list`,
				method: "get",
				params: params
			}).then(res => {
				if(res.data&&res.data.code==0){
					this.newsList = res.data.data.list
				}
			});
		},
		newsDetailClick(row){
			this.newsDetail = row
			this.newsVisible = true
		},
		getautohomeCount() {
			this.$http({
				url: `autohome/count`,
				method: "get"
			}).then(({
				data
			}) => {
				if (data && data.code == 0) {
					this.autohomeCount = data.data
				}
			})
		},
		autohomeChat1(e=null) {
			this.$nextTick(()=>{
				var autohomeChart1 = echarts.init(document.getElementById("autohomeChart1"),'macarons');
				let params = {
					order: 'desc',
					orderType: 'y',
				}
				this.$http({
					url: `autohome/value/title/liulan`,
					method: "get",
					params
				}).then(({ data }) => {
					if (data && data.code === 0) {
						let res = data.data||[];
						// 统计图设置对了吗
						let xAxis = [];
						let yAxis = [];
						let pArray = []
						for(let i=0;i<res.length;i++){
							if(this.boardBase&&i==this.boardBase.lineNum){
								break;
							}
							xAxis.push(res[i].title);
							yAxis.push(parseFloat((res[i].total)));
							pArray.push({
								value: parseFloat((res[i].total)),
								name: res[i].title
							})
						}
						var option = {};
						let titleObj = this.line.title
						titleObj.text = '新能源资讯浏览量'
						
						const legendObj = this.line.legend
						let tooltipObj = { trigger: 'item',formatter: '{b} : {c}'}
						tooltipObj = Object.assign(tooltipObj , this.line.tooltip?this.line.tooltip:{})
						let xAxisObj = this.line.xAxis
						xAxisObj.type = 'category'
						xAxisObj.data = xAxis
						
						let yAxisObj = this.line.yAxis
						yAxisObj.type = 'value'
						const gridObj = this.line.grid
						
						let seriesObj = {
							data: yAxis,
							type: 'line',
						}
						seriesObj = Object.assign(seriesObj , this.line.series)
						option = {
							backgroundColor: this.line.backgroundColor,
							color: this.line.color,
							title: titleObj,
							legend: legendObj,
							grid: gridObj,
							tooltip: tooltipObj,
							xAxis: xAxisObj,
							yAxis: yAxisObj,
							series: [seriesObj]
						};
						// 使用刚指定的配置项和数据显示图表。
						autohomeChart1.setOption(option);
				
						//根据窗口的大小变动图表
						window.onresize = function() {
							autohomeChart1.resize();
						};
					}else{
						this.$message({
							message: data.msg,
							type: "warning",
							duration: 1500,
						})
					}
				});
			})
		},

		autohomeChat2(e=null) {
			this.$nextTick(()=>{

				var autohomeChart2 = echarts.init(document.getElementById("autohomeChart2"),'macarons');
				let params = {
				}
				this.$http({
					url: "autohome/group/zuozhe",
					method: "get",
					params
				}).then(({ data }) => {
					if (data && data.code === 0) {
						let res = data.data||[];
						// 统计图设置对了吗
						let xAxis = [];
						let yAxis = [];
						let pArray = []
						for(let i=0;i<res.length;i++){
							if(this.boardBase&&i==this.boardBase.pieNum){
								break;
							}
							xAxis.push(res[i].zuozhe);
							yAxis.push(parseFloat((res[i].total)));
							pArray.push({
								value: parseFloat((res[i].total)),
								name: res[i].zuozhe
							})
						}
						var option = {};
						let titleObj = this.pie.title
						titleObj.text = '新能源资讯作者发布次数'
						
						const legendObj = this.pie.legend
						let tooltipObj = {trigger: 'item',formatter: '{b} : {c} ({d}%)'}
						tooltipObj = Object.assign(tooltipObj , this.pie.tooltip?this.pie.tooltip:{})
						
						let seriesObj = {
							type: 'pie',
							radius: '55%',
							center: ['50%', '60%'],
							data: pArray,
							emphasis: {
								itemStyle: {
									shadowBlur: 10,
									shadowOffsetX: 0,
									shadowColor: 'rgba(0, 0, 0, 0.5)'
								}
							}
						}
						seriesObj = Object.assign(seriesObj , this.pie.series)
						const gridObj = this.pie.grid
						option = {
							backgroundColor: this.pie.backgroundColor,
							color: this.pie.color,
							title: titleObj,
							legend: legendObj,
							tooltip: tooltipObj,
							series: [seriesObj],
							grid: gridObj
						};
						// 使用刚指定的配置项和数据显示图表。
						autohomeChart2.setOption(option);
				
						//根据窗口的大小变动图表
						window.onresize = function() {
							autohomeChart2.resize();
						};
					}else{
						this.$message({
							message: data.msg,
							type: "warning",
							duration: 1500,
						})
					}
				});
			})
		},

		getxingyezixunCount() {
			this.$http({
				url: `xingyezixun/count`,
				method: "get"
			}).then(({
				data
			}) => {
				if (data && data.code == 0) {
					this.xingyezixunCount = data.data
				}
			})
		},
		xingyezixunChat1(e=null) {
			this.$nextTick(()=>{
				var xingyezixunChart1 = echarts.init(document.getElementById("xingyezixunChart1"),'macarons');
				let params = {
				}
				this.$http({
					url: `xingyezixun/value/zixunbiaoti/clicknum`,
					method: "get",
					params
				}).then(({ data }) => {
					if (data && data.code === 0) {
						let res = data.data||[];
						// 统计图设置对了吗
						let xAxis = [];
						let yAxis = [];
						let pArray = []
						for(let i=0;i<res.length;i++){
							if(this.boardBase&&i==this.boardBase.barNum){
								break;
							}
							xAxis.push(res[i].zixunbiaoti);
							yAxis.push(parseFloat((res[i].total)));
							pArray.push({
								value: parseFloat((res[i].total)),
								name: res[i].zixunbiaoti
							})
						}
						var option = {};
						let titleObj = this.bar.title
						titleObj.text = '行业资讯浏览量'
						
						const legendObj = this.bar.legend
						let tooltipObj = {trigger: 'item',formatter: '{b} : {c}'}
						tooltipObj = Object.assign(tooltipObj , this.bar.tooltip?this.bar.tooltip:{})
				
						let xAxisObj = this.bar.xAxis
						xAxisObj.type = 'category'
						xAxisObj.data = xAxis
						
						let yAxisObj = this.bar.yAxis
						yAxisObj.type = 'value'
						let seriesObj = {
							data: yAxis,
							type: 'bar',
						}
						seriesObj = Object.assign(seriesObj , this.bar.series)
						const gridObj = this.bar.grid
						
						option = {
							backgroundColor: this.bar.backgroundColor,
							color: this.bar.color,
							title: titleObj,
							legend: legendObj,
							grid: gridObj,
							tooltip: tooltipObj,
							xAxis: xAxisObj,
							yAxis: yAxisObj,
							series: [seriesObj]
						};
						// 使用刚指定的配置项和数据显示图表。
						xingyezixunChart1.setOption(option);
				
						//根据窗口的大小变动图表
						window.onresize = function() {
							xingyezixunChart1.resize();
						};
					}else{
						this.$message({
							message: data.msg,
							type: "warning",
							duration: 1500,
						})
					}
				});
			})
		},

		xingyezixunChat2(e=null) {
			this.$nextTick(()=>{

				var xingyezixunChart2 = echarts.init(document.getElementById("xingyezixunChart2"),'macarons');
				let params = {
				}
				this.$http({
					url: `xingyezixun/value/zixunbiaoti/storeupnum`,
					method: "get",
					params
				}).then(({ data }) => {
					if (data && data.code === 0) {
						let res = data.data||[];
						// 统计图设置对了吗
						let xAxis = [];
						let yAxis = [];
						let pArray = []
						for(let i=0;i<res.length;i++){
							if(this.boardBase&&i==this.boardBase.funnelNum){
								break;
							}
							xAxis.push(res[i].zixunbiaoti);
							yAxis.push(parseFloat((res[i].total)));
							pArray.push({
								value: parseFloat((res[i].total)),
								name: res[i].zixunbiaoti
							})
						}
						var option = {};
						let titleObj = this.funnel.title
						titleObj.text = '行业资讯收藏量'
						
						let legendObj = {
							data: xAxis,
						}
						legendObj = Object.assign(legendObj , this.funnel.legend)
						let tooltipObj = {trigger: 'item',formatter: '{b} : {c}'}
						tooltipObj = Object.assign(tooltipObj , this.funnel.tooltip?this.funnel.tooltip:{})
						let seriesObj = {
							name: '行业资讯收藏量',
							data: pArray,
							type: 'funnel',
							left: '10%',
							top: 60,
							bottom: 60,
							width: '80%',
							minSize: '0%',
							maxSize: '100%',
						}
						seriesObj = Object.assign(seriesObj , this.funnel.series)
						const gridObj = this.funnel.grid
						option = {
							backgroundColor: this.funnel.backgroundColor,
							color: this.funnel.color,
							title: titleObj,
							legend: legendObj,
							tooltip: tooltipObj,
							series: seriesObj,
							grid: gridObj
						}
						// 使用刚指定的配置项和数据显示图表。
						xingyezixunChart2.setOption(option);
				
						//根据窗口的大小变动图表
						window.onresize = function() {
							xingyezixunChart2.resize();
						};
					}else{
						this.$message({
							message: data.msg,
							type: "warning",
							duration: 1500,
						})
					}
				});
			})
		},

		xingyezixunChat3(e=null) {
			this.$nextTick(()=>{

				var xingyezixunChart3 = echarts.init(document.getElementById("xingyezixunChart3"),'macarons');
				let params = {
				}
				this.$http({
					url: "xingyezixun/group/zixunfenlei",
					method: "get",
					params
				}).then(({ data }) => {
					if (data && data.code === 0) {
						let res = data.data||[];
						// 统计图设置对了吗
						let xAxis = [];
						let yAxis = [];
						let pArray = []
						for(let i=0;i<res.length;i++){
							if(this.boardBase&&i==this.boardBase.pieNum){
								break;
							}
							xAxis.push(res[i].zixunfenlei);
							yAxis.push(parseFloat((res[i].total)));
							pArray.push({
								value: parseFloat((res[i].total)),
								name: res[i].zixunfenlei
							})
						}
						var option = {};
						let titleObj = this.pie.title
						titleObj.text = '资讯分类'
						
						const legendObj = this.pie.legend
						let tooltipObj = {trigger: 'item',formatter: '{b} : {c} ({d}%)'}
						tooltipObj = Object.assign(tooltipObj , this.pie.tooltip?this.pie.tooltip:{})
						
						let seriesObj = {
							type: 'pie',
							radius: ['25%', '55%'],
							roseType: 'area',
							center: ['50%', '60%'],
							data: pArray,
							emphasis: {
								itemStyle: {
									shadowBlur: 10,
									shadowOffsetX: 0,
									shadowColor: 'rgba(0, 0, 0, 0.5)'
								}
							}
						}
						seriesObj = Object.assign(seriesObj , this.pie.series)
						const gridObj = this.pie.grid
						
						option = {
							backgroundColor: this.pie.backgroundColor,
							color: this.pie.color,
							title: titleObj,
							legend: legendObj,
							tooltip: tooltipObj,
							series: [seriesObj],
							grid: gridObj
						};
						// 使用刚指定的配置项和数据显示图表。
						xingyezixunChart3.setOption(option);
						//根据窗口的大小变动图表
						window.onresize = function() {
							xingyezixunChart3.resize();
						};
					}else{
						this.$message({
							message: data.msg,
							type: "warning",
							duration: 1500,
						})
					}
				});
			})
		},
		getxingyezixunfaburenOptions4() {
			this.$http.get('option/xingyezixun/faburen',
			).then(rs=>{
				this.xingyezixunChartOptions4 = rs.data.data
			})
		},
		xingyezixunChat4(e=null) {
			if(this.changeStatQuery(['users'])) {
				document.getElementById('xingyezixunChart4').setAttribute('style','width: 100%;height: calc(100% - 50px)')
			}
			this.$nextTick(()=>{

				var xingyezixunChart4 = echarts.init(document.getElementById("xingyezixunChart4"),'macarons');
				let params = {
				}
				if(this.xingyezixunchartQuery4.faburen) {
					params.conditionColumn = 'faburen'
					params.conditionValue = this.xingyezixunchartQuery4.faburen
				}
				this.$http({
					url: "xingyezixun/group/fabushijian",
					method: "get",
					params
				}).then(({ data }) => {
					if (data && data.code === 0) {
						let res = data.data||[];
						// 统计图设置对了吗
						let xAxis = [];
						let yAxis = [];
						let pArray = []
						for(let i=0;i<res.length;i++){
							if(this.boardBase&&i==this.boardBase.pieNum){
								break;
							}
							xAxis.push(res[i].fabushijian);
							yAxis.push(parseFloat((res[i].total)));
							pArray.push({
								value: parseFloat((res[i].total)),
								name: res[i].fabushijian
							})
						}
						var option = {};
						let titleObj = this.pie.title
						titleObj.text = '日行业资讯发布量'
						
						const legendObj = this.pie.legend
						let tooltipObj = {trigger: 'item',formatter: '{b} : {c} ({d}%)'}
						tooltipObj = Object.assign(tooltipObj , this.pie.tooltip?this.pie.tooltip:{})
						
						let seriesObj = {
							type: 'pie',
							radius: '55%',
							center: ['50%', '60%'],
							data: pArray,
							emphasis: {
								itemStyle: {
									shadowBlur: 10,
									shadowOffsetX: 0,
									shadowColor: 'rgba(0, 0, 0, 0.5)'
								}
							}
						}
						seriesObj = Object.assign(seriesObj , this.pie.series)
						const gridObj = this.pie.grid
						option = {
							backgroundColor: this.pie.backgroundColor,
							color: this.pie.color,
							title: titleObj,
							legend: legendObj,
							tooltip: tooltipObj,
							series: [seriesObj],
							grid: gridObj
						};
						// 使用刚指定的配置项和数据显示图表。
						xingyezixunChart4.setOption(option);

						//根据窗口的大小变动图表
						window.onresize = function() {
							xingyezixunChart4.resize();
						};
					}else{
						this.$message({
							message: data.msg,
							type: "warning",
							duration: 1500,
						})
					}
				});
			})
		},
	}
};
</script>
<style lang="scss" scoped>
	.home-content {
		padding: 0 30px 30px;
		background: url(http://codegen.caihongy.cn/20250919/2c80b3fb2558476da48a42912f355e53.png) no-repeat center top / cover;
		display: flex;
		width: 100%;
		min-height: 100vh;
		flex-wrap: wrap;
		.home-title {
			padding: 10px 0 0;
			box-shadow: none;
			margin: 10px 0 0;
			display: flex;
			width: 100%;
			justify-content: center;
			align-items: center;
			transition: 0.3s;
			.titles {
				padding: 0;
				color: #333;
				font-size: 30px;
				line-height: 60px;
				span {
				}
			}
		}
		.home-title:hover {
			transform: translate3d(0, 0px, 0);
		}
		.statis-box {
			margin: 20px 0;
			background: none;
			display: flex;
			width: 100%;
			align-items: center;
			flex-wrap: wrap;
			.statis1 {
				border: 0px solid #e5f0f9;
				border-radius: 8px;
				box-shadow: none;
				padding: 20px;
				margin: 10px;
				background: #fff;
				display: flex;
				width: calc(25% - 20px);
				align-items: center;
				transition: 0.3s;
				height: 130px;
				.left {
					display: flex;
					width: 40px;
					justify-content: center;
					align-items: center;
					height: 40px;
					order: 2;
					.iconfont {
						border-radius: 0;
						padding: 0;
						color: #599BFF;
						background: none;
						font-weight: bold;
						width: 48px;
						font-size: 32px;
						line-height: 40px;
						text-align: center;
						height: 40px;
					}
				}
				.right {
					flex-direction: column;
					display: flex;
					width: 100%;
					justify-content: space-between;
					.num {
						margin: 5px 0;
						color: #212D3F;
						font-weight: 700;
						font-size: 18px;
						line-height: 24px;
						height: 24px;
						order: 2;
					}
					.name {
						margin: 5px 0;
						color: #212D3F;
						font-weight: 700;
						font-size: 18px;
						line-height: 24px;
						height: 24px;
					}
				}
			}
			.statis1:hover {
				box-shadow: 0 3px 0px rgba(0,0,0,.1);
				transform: translate3d(0, -6px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
			.statis2 {
				border: 0px solid #e5f0f9;
				border-radius: 8px;
				box-shadow: none;
				padding: 20px;
				margin: 10px;
				background: #fff;
				display: flex;
				width: calc(25% - 20px);
				align-items: center;
				transition: 0.3s;
				height: 130px;
				.left {
					background: none;
					display: flex;
					width: 48px;
					justify-content: center;
					align-items: center;
					height: 48px;
					order: 2;
					.iconfont {
						border-radius: 0;
						padding: 0;
						color: #06B867;
						background: none;
						font-weight: bold;
						width: 48px;
						font-size: 32px;
						line-height: 40px;
						text-align: center;
						height: 40px;
					}
				}
				.right {
					flex-direction: column;
					display: flex;
					width: 100%;
					justify-content: space-between;
					.num {
						margin: 5px 0;
						color: #212D3F;
						font-weight: 700;
						font-size: 18px;
						line-height: 24px;
						height: 24px;
						order: 2;
					}
					.name {
						margin: 5px 0;
						color: #212D3F;
						font-weight: 700;
						font-size: 18px;
						line-height: 24px;
						height: 24px;
					}
				}
			}
			.statis2:hover {
				box-shadow: 0 3px 0px rgba(0,0,0,.1);
				transform: translate3d(0, -6px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
			.statis3 {
				border: 0px solid #e5f0f9;
				border-radius: 8px;
				box-shadow: none;
				padding: 20px;
				margin: 10px;
				background: #fff;
				display: flex;
				width: calc(25% - 20px);
				align-items: center;
				transition: 0.3s;
				height: 130px;
				.left {
					background: none;
					display: flex;
					width: 48px;
					justify-content: center;
					align-items: center;
					height: 48px;
					order: 2;
					.iconfont {
						border-radius: 0;
						padding: 0;
						color: #F0D164;
						background: none;
						font-weight: bold;
						width: 48px;
						font-size: 32px;
						line-height: 40px;
						text-align: center;
						height: 40px;
					}
				}
				.right {
					flex-direction: column;
					display: flex;
					width: 100%;
					justify-content: space-between;
					.num {
						margin: 5px 0;
						color: #212D3F;
						font-weight: 700;
						font-size: 18px;
						line-height: 24px;
						height: 24px;
						order: 2;
					}
					.name {
						margin: 5px 0;
						color: #212D3F;
						font-weight: 700;
						font-size: 18px;
						line-height: 24px;
						height: 24px;
					}
				}
			}
			.statis3:hover {
				box-shadow: 0 3px 0px rgba(0,0,0,.1);
				transform: translate3d(0, -6px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
			.statis4 {
				border: 0px solid #e5f0f9;
				border-radius: 8px;
				box-shadow: none;
				padding: 20px;
				margin: 10px;
				background: #fff;
				display: flex;
				width: calc(25% - 20px);
				align-items: center;
				transition: 0.3s;
				height: 130px;
				.left {
					background: none;
					display: flex;
					width: 48px;
					justify-content: center;
					align-items: center;
					height: 48px;
					order: 2;
					.iconfont {
						border-radius: 0;
						padding: 0;
						color: #599BFF;
						background: none;
						font-weight: bold;
						width: 48px;
						font-size: 32px;
						line-height: 40px;
						text-align: center;
						height: 40px;
					}
				}
				.right {
					flex-direction: column;
					display: flex;
					width: 100%;
					justify-content: space-between;
					.num {
						margin: 5px 0;
						color: #212D3F;
						font-weight: 700;
						font-size: 18px;
						line-height: 24px;
						height: 24px;
						order: 2;
					}
					.name {
						margin: 5px 0;
						color: #212D3F;
						font-weight: 700;
						font-size: 18px;
						line-height: 24px;
						height: 24px;
					}
				}
			}
			.statis4:hover {
				box-shadow: 0 3px 0px rgba(0,0,0,.1);
				transform: translate3d(0, -6px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
			.statis5 {
				border: 0px solid #e5f0f9;
				border-radius: 8px;
				box-shadow: none;
				padding: 20px;
				margin: 10px;
				background: #fff;
				display: flex;
				width: calc(25% - 20px);
				align-items: center;
				transition: 0.3s;
				height: 130px;
				.left {
					background: none;
					display: flex;
					width: 48px;
					justify-content: center;
					align-items: center;
					height: 48px;
					order: 2;
					.iconfont {
						border-radius: 0;
						padding: 0;
						color: #00C07B;
						background: none;
						font-weight: bold;
						width: 48px;
						font-size: 32px;
						line-height: 40px;
						text-align: center;
						height: 40px;
					}
				}
				.right {
					flex-direction: column;
					display: flex;
					width: 100%;
					justify-content: space-between;
					.num {
						margin: 5px 0;
						color: #212D3F;
						font-weight: 700;
						font-size: 18px;
						line-height: 24px;
						height: 24px;
						order: 2;
					}
					.name {
						margin: 5px 0;
						color: #212D3F;
						font-weight: 700;
						font-size: 18px;
						line-height: 24px;
						height: 24px;
					}
				}
			}
			.statis5:hover {
				box-shadow: 0 3px 0px rgba(0,0,0,.1);
				transform: translate3d(0, -6px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
			.statis6 {
				border: 0px solid #e5f0f9;
				border-radius: 8px;
				box-shadow: none;
				padding: 20px;
				margin: 10px;
				background: #fff;
				display: flex;
				width: calc(25% - 20px);
				align-items: center;
				transition: 0.3s;
				height: 130px;
				.left {
					background: none;
					display: flex;
					width: 48px;
					justify-content: center;
					align-items: center;
					height: 48px;
					order: 2;
					.iconfont {
						border-radius: 0;
						padding: 0;
						color: #F0D164;
						background: none;
						font-weight: bold;
						width: 48px;
						font-size: 32px;
						line-height: 40px;
						text-align: center;
						height: 40px;
					}
				}
				.right {
					flex-direction: column;
					display: flex;
					width: 100%;
					justify-content: space-between;
					.num {
						margin: 5px 0;
						color: #212D3F;
						font-weight: 700;
						font-size: 18px;
						line-height: 24px;
						height: 24px;
						order: 2;
					}
					.name {
						margin: 5px 0;
						color: #212D3F;
						font-weight: 700;
						font-size: 18px;
						line-height: 24px;
						height: 24px;
					}
				}
			}
			.statis6:hover {
				box-shadow: 0 3px 0px rgba(0,0,0,.1);
				transform: translate3d(0, -6px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
			.statis7 {
				border: 0px solid #e5f0f9;
				border-radius: 8px;
				box-shadow: none;
				padding: 20px;
				margin: 10px;
				background: #fff;
				display: flex;
				width: calc(25% - 20px);
				align-items: center;
				transition: 0.3s;
				height: 130px;
				.left {
					background: none;
					display: flex;
					width: 48px;
					justify-content: center;
					align-items: center;
					height: 48px;
					order: 2;
					.iconfont {
						border-radius: 0;
						padding: 0;
						color: #599BFF;
						background: none;
						font-weight: bold;
						width: 48px;
						font-size: 32px;
						line-height: 40px;
						text-align: center;
						height: 40px;
					}
				}
				.right {
					flex-direction: column;
					display: flex;
					width: 100%;
					justify-content: space-between;
					.num {
						margin: 5px 0;
						color: #212D3F;
						font-weight: 700;
						font-size: 18px;
						line-height: 24px;
						height: 24px;
						order: 2;
					}
					.name {
						margin: 5px 0;
						color: #212D3F;
						font-weight: 700;
						font-size: 18px;
						line-height: 24px;
						height: 24px;
					}
				}
			}
			.statis7:hover {
				box-shadow: 0 3px 0px rgba(0,0,0,.1);
				transform: translate3d(0, -6px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
			.statis8 {
				border: 0px solid #e5f0f9;
				border-radius: 8px;
				box-shadow: none;
				padding: 20px;
				margin: 10px;
				background: #fff;
				display: flex;
				width: calc(25% - 20px);
				align-items: center;
				transition: 0.3s;
				height: 130px;
				.left {
					background: none;
					display: flex;
					width: 48px;
					justify-content: center;
					align-items: center;
					height: 48px;
					order: 2;
					.iconfont {
						border-radius: 0;
						padding: 0;
						color: #06B867;
						background: none;
						font-weight: bold;
						width: 48px;
						font-size: 32px;
						line-height: 40px;
						text-align: center;
						height: 40px;
					}
				}
				.right {
					flex-direction: column;
					display: flex;
					width: 100%;
					justify-content: space-between;
					.num {
						margin: 5px 0;
						color: #212D3F;
						font-weight: 700;
						font-size: 18px;
						line-height: 24px;
						height: 24px;
						order: 2;
					}
					.name {
						margin: 5px 0;
						color: #212D3F;
						font-weight: 700;
						font-size: 18px;
						line-height: 24px;
						height: 24px;
					}
				}
			}
			.statis8:hover {
				box-shadow: 0 3px 0px rgba(0,0,0,.1);
				transform: translate3d(0, -6px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
			.statis9 {
				border: 0px solid #e5f0f9;
				border-radius: 8px;
				box-shadow: none;
				padding: 20px;
				margin: 10px;
				background: #fff;
				display: flex;
				width: calc(25% - 20px);
				align-items: center;
				transition: 0.3s;
				height: 130px;
				.left {
					background: none;
					display: flex;
					width: 48px;
					justify-content: center;
					align-items: center;
					height: 48px;
					order: 2;
					.iconfont {
						border-radius: 0;
						padding: 0;
						color: #F0D164;
						background: none;
						font-weight: bold;
						width: 48px;
						font-size: 32px;
						line-height: 40px;
						text-align: center;
						height: 40px;
					}
				}
				.right {
					flex-direction: column;
					display: flex;
					width: 100%;
					justify-content: space-between;
					.num {
						margin: 5px 0;
						color: #212D3F;
						font-weight: 700;
						font-size: 18px;
						line-height: 24px;
						height: 24px;
						order: 2;
					}
					.name {
						margin: 5px 0;
						color: #212D3F;
						font-weight: 700;
						font-size: 18px;
						line-height: 24px;
						height: 24px;
					}
				}
			}
			.statis9:hover {
				box-shadow: 0 3px 0px rgba(0,0,0,.1);
				transform: translate3d(0, -6px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
			.statis10 {
				border: 0px solid #e5f0f9;
				border-radius: 8px;
				box-shadow: none;
				padding: 20px;
				margin: 10px;
				background: #fff;
				display: flex;
				width: calc(25% - 20px);
				align-items: center;
				transition: 0.3s;
				height: 130px;
				.left {
					background: none;
					display: flex;
					width: 48px;
					justify-content: center;
					align-items: center;
					height: 48px;
					order: 2;
					.iconfont {
						border-radius: 0;
						padding: 0;
						color: #599BFF;
						background: none;
						font-weight: bold;
						width: 48px;
						font-size: 32px;
						line-height: 40px;
						text-align: center;
						height: 40px;
					}
				}
				.right {
					flex-direction: column;
					display: flex;
					width: 100%;
					justify-content: space-between;
					.num {
						margin: 5px 0;
						color: #212D3F;
						font-weight: 700;
						font-size: 18px;
						line-height: 24px;
						height: 24px;
						order: 2;
					}
					.name {
						margin: 5px 0;
						color: #212D3F;
						font-weight: 700;
						font-size: 18px;
						line-height: 24px;
						height: 24px;
					}
				}
			}
			.statis10:hover {
				box-shadow: 0 3px 0px rgba(0,0,0,.1);
				transform: translate3d(0, -6px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
		}
		.news-box {
			border: 0;
			padding: 30px 20px ;
			margin: 10px;
			display: flex;
			transition: 0.3s;
			border-radius: 10px;
			box-shadow: none;
			flex-direction: column;
			flex: 2;
			background: #fff;
			width: calc(50% - 20px);
			justify-content: center;
			align-items: center;
			order: 2;
			height: 360px;
			.news-title {
				margin: 10px 0 0 0;
				color: #000;
				font-weight: 600;
				width: 100%;
				font-size: 18px;
			}
			.news-list {
				padding: 15px 0 0 0;
				display: flex;
				width: 100%;
				border-color: #DBDBDB;
				border-width: 0 0 1px 0;
				justify-content: space-between;
				align-items: center;
				border-style: solid;
				flex-wrap: wrap;
			}
			.news-item {
				cursor: pointer;
				padding: 2px 16px ;
				margin: 0;
				display: flex;
				width: calc(100% - 0px);
				border-color: #DBDBDB;
				border-width: 1px 1px 0 1px ;
				justify-content: space-between;
				align-items: center;
				border-style: solid;
				.news-text {
					overflow: hidden;
					color: #212D3F;
					white-space: nowrap;
					flex: 1;
					font-weight: 500;
					width: 100%;
					font-size: 16px;
					line-height: 2;
					text-overflow: ellipsis;
				}
				.news-img-box {
					margin: 0 10px 0 0;
					overflow: hidden;
					display: none;
					width: auto;
					height: auto;
					img {
						object-fit: cover;
						width: 60px;
						height: 60px;
					}
				}
				.news-desc {
					overflow: hidden;
					color: #666;
					white-space: nowrap;
					flex: 1;
					display: none;
					width: 100%;
					text-overflow: ellipsis;
				}
				.news-time {
					color: #5D5D5D;
					font-weight: 400;
					font-size: 14px;
				}
			}
		}
		.news-box:hover {
			box-shadow: 0 3px 0px rgba(0,0,0,.1);
			transform: translate3d(0, -6px, 0);
			z-index: 1;
			background: rgba(255,255,255,1);
		}
		// echarts6
		.type6 {
			padding: 0;
			align-content: flex-start;
			background: none;
			display: flex;
			width: 100%;
			justify-content: space-between;
			flex-wrap: wrap;
			height: auto;
			.echarts1 {
				border-radius: 10px;
				padding: 20px;
				box-shadow: none;
				margin: 10px;
				background: rgba(255,255,255,1);
				width: calc(50% - 20px);
				transition: 0.3s;
				height: 550px;
			}
			.echarts1:hover {
				box-shadow: 0 3px 0px rgba(0,0,0,.1);
				transform: translate3d(0, -6px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
			.echarts2 {
				border-radius: 10px;
				padding: 20px;
				box-shadow: none;
				margin: 10px;
				background: rgba(255,255,255,1);
				width: calc(50% - 20px);
				transition: 0.3s;
				height: 550px;
			}
			.echarts2:hover {
				box-shadow: 0 3px 0px rgba(0,0,0,.1);
				transform: translate3d(0, -6px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
			.echarts3 {
				border-radius: 10px;
				padding: 20px;
				box-shadow: none;
				margin: 10px;
				background: rgba(255,255,255,1);
				width: calc(50% - 20px);
				transition: 0.3s;
				height: 550px;
			}
			.echarts3:hover {
				box-shadow: 0 3px 0px rgba(0,0,0,.1);
				transform: translate3d(0, -6px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
			.echarts4 {
				border-radius: 10px;
				padding: 20px;
				box-shadow: none;
				margin: 10px;
				background: rgba(255,255,255,1);
				width: calc(50% - 20px);
				transition: 0.3s;
				height: 550px;
			}
			.echarts4:hover {
				box-shadow: 0 3px 0px rgba(0,0,0,.1);
				transform: translate3d(0, -6px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
			.echarts5 {
				border-radius: 10px;
				padding: 20px;
				box-shadow: none;
				margin: 10px;
				background: rgba(255,255,255,1);
				width: calc(50% - 20px);
				transition: 0.3s;
				height: 550px;
			}
			.echarts5:hover {
				box-shadow: 0 3px 0px rgba(0,0,0,.1);
				transform: translate3d(0, -6px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
			.echarts6 {
				border-radius: 10px;
				padding: 20px;
				box-shadow: none;
				margin: 10px;
				background: rgba(255,255,255,1);
				width: calc(50% - 20px);
				transition: 0.3s;
				height: 550px;
			}
			.echarts6:hover {
				box-shadow: 0 3px 0px rgba(0,0,0,.1);
				transform: translate3d(0, -6px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
		}
	}
	
	.echarts-flag-2 {
		display: flex;
		flex-wrap: wrap;
		justify-content: space-between;
		padding: 10px 20px;
		background: rebeccapurple;
	
		&>div {
			width: 32%;
			height: 300px;
			margin: 10px 0;
			background: rgba(255,255,255,.1);
			border-radius: 8px;
			padding: 10px 20px;
		}
	}
	.animate__animated {
		animation-fill-mode: none;
	}
</style>
