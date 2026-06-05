<template>
	<div class="content" :style='{"alignContent":"flex-start","overflow":"hidden","background":"#000","flexDirection":"column","display":"flex","width":"100%","position":"relative","height":"100%"}'>
		<div :style='{"padding":"25px 0 0","margin":"0","background":"url(http://codegen.caihongy.cn/20251118/80caa41b65f042b18210d8dee104b4d3.png) no-repeat center / 100% 100%, url(http://codegen.caihongy.cn/20251118/5bada34ec28e4490b62887d4d6d5ce7e.gif) no-repeat left center / 60px auto,url(http://codegen.caihongy.cn/20251118/5bada34ec28e4490b62887d4d6d5ce7e.gif) no-repeat right center / 60px auto","display":"flex","width":"100%","position":"relative","justifyContent":"center","height":"80px"}'>
			<!-- 标题 -->
			<div :style='{"margin":"0","fontSize":"20px","color":"#fff","textAlign":"center","background":"none","fontWeight":"700"}'>欢迎使用 {{this.$project.projectName}}</div>
			<!-- 时间 -->
			<div :style='{"alignItems":"center","color":"#42cc8a","top":"50px","display":"flex","fontSize":"16px","position":"absolute","right":"80px"}'>
				<div :style='{"margin":"0 30px 0 0","fontSize":"16px","whiteSpace":"nowrap","color":"#fff","display":"inline-block"}'>{{ dates }}</div> 
				<div @click="backClick" :style='{"cursor":"pointer","color":"inherit"}'>{{frontType==1?'返回':'管理系统'}}</div>
			</div>
		</div>
		<div :style='{"padding":"10px 0","flex":"auto","background":"none","display":"flex","width":"100%","justifyContent":"space-between","height":"0"}'>
			<div :style='{"width":"25%","padding":"0","flexDirection":"column","background":"none","display":"flex","gap":"10px"}'>
				<div class="echarts1">
					<div :style='{"padding":"0","margin":"0","textAlign":"center","background":"url(http://codegen.caihongy.cn/20251118/2da4e59a1e2040a8b5726111ef573b48.png) no-repeat center / 100% 100%","flex":"none","display":"flex","width":"100%","justifyContent":"space-between","height":"auto"}'>
						<div :style='{"padding":"0 0 0 50px","color":"#fff","textAlign":"left","background":"none","fontSize":"16px","lineHeight":"40px","fontWeight":"600","height":"40px"}'>
							新能源资讯浏览量
						</div>
					</div>
					<div :style='{"width":"100%","flex":"auto","background":"url(http://codegen.caihongy.cn/20251118/073929b9a3bc4164b6e53f03896fc462.png) no-repeat center / 100% 100%","height":"0"}'>
						<div id="autohomeChart1" style="width:100%;height:100%;"></div>
					</div>
				</div>
				<div class="echarts2">
					<div :style='{"padding":"0","margin":"0","textAlign":"center","background":"url(http://codegen.caihongy.cn/20251118/2da4e59a1e2040a8b5726111ef573b48.png) no-repeat center / 100% 100%","flex":"none","display":"flex","width":"100%","justifyContent":"space-between","height":"auto"}'>
						<div :style='{"padding":"0 0 0 50px","color":"#fff","textAlign":"left","background":"none","fontSize":"16px","lineHeight":"40px","fontWeight":"600","height":"40px"}'>
							新能源资讯作者发布次数
						</div>
					</div>
					<div :style='{"width":"100%","flex":"auto","background":"url(http://codegen.caihongy.cn/20251118/073929b9a3bc4164b6e53f03896fc462.png) no-repeat center / 100% 100%","height":"0"}'>
						<div id="autohomeChart2" style="width:100%;height:100%;"></div>
					</div>
				</div>
				<div class="echarts3">
					<div :style='{"padding":"0","margin":"0","textAlign":"center","background":"url(http://codegen.caihongy.cn/20251118/2da4e59a1e2040a8b5726111ef573b48.png) no-repeat center / 100% 100%","flex":"none","display":"flex","width":"100%","justifyContent":"space-between","height":"auto"}'>
						<div :style='{"padding":"0 0 0 50px","color":"#fff","textAlign":"left","background":"none","fontSize":"16px","lineHeight":"40px","fontWeight":"600","height":"40px"}'>
							行业资讯浏览量
						</div>
					</div>
					<div :style='{"width":"100%","flex":"auto","background":"url(http://codegen.caihongy.cn/20251118/073929b9a3bc4164b6e53f03896fc462.png) no-repeat center / 100% 100%","height":"0"}'>
						<div id="xingyezixunChart3" style="width:100%;height:100%;"></div>
					</div>
				</div>
			</div>
			<div :style='{"width":"calc(50% - 40px)","padding":"0","flexDirection":"column","display":"flex"}'>
				<!-- 统计 -->
				<div :style='{"padding":"0","margin":"0","color":"#fff","alignItems":"center","display":"flex","justifyContent":"center","alignContent":"center","background":"none","gap":"10px","width":"100%","fontSize":"14px","height":"90px","order":"1"}'>

					<div :style='{"filter":"none","margin":"0","alignItems":"center","background":"url(http://codegen.caihongy.cn/20251118/7532635c666840238bff774a5eae8e4c.png) no-repeat center / 100% 100%","flexDirection":"column","flex":"1 1 auto","display":"flex","width":"150px","position":"relative","justifyContent":"center","height":"90px","maxWidth":"200px"}'>
						<div :style='{"width":"12px","margin":"0 0 0 20px","background":"#2097db","display":"none","height":"12px"}'></div>
						<div :style='{"padding":"0","alignItems":"center","flexDirection":"column","display":"flex","width":"100%","justifyContent":"center","height":"100%"}'>
							<div :style='{"lineHeight":"24px","fontSize":"inherit","position":"relative","color":"inherit","top":"0","height":"24px"}'>新能源资讯总数</div>
							<div :style='{"lineHeight":"40px","fontSize":"24px","color":"#42cc8a","fontWeight":"bold","height":"40px","order":"20"}'>{{autohomeCount}}</div>
						</div>
					</div>

					<div :style='{"filter":"none","margin":"0","alignItems":"center","background":"url(http://codegen.caihongy.cn/20251118/7532635c666840238bff774a5eae8e4c.png) no-repeat center / 100% 100%","flexDirection":"column","flex":"1 1 auto","display":"flex","width":"150px","position":"relative","justifyContent":"center","height":"90px","maxWidth":"200px"}'>
						<div :style='{"width":"12px","margin":"0 0 0 20px","background":"#2097db","display":"none","height":"12px"}'></div>
						<div :style='{"padding":"0","alignItems":"center","flexDirection":"column","display":"flex","width":"100%","justifyContent":"center","height":"100%"}'>
							<div :style='{"lineHeight":"24px","fontSize":"inherit","position":"relative","color":"inherit","top":"0","height":"24px"}'>行业资讯总数</div>
							<div :style='{"lineHeight":"40px","fontSize":"24px","color":"#42cc8a","fontWeight":"bold","height":"40px","order":"20"}'>{{xingyezixunCount}}</div>
						</div>
					</div>
				</div>
				<div class="echarts7">
					<div :style='{"padding":"0","margin":"0","textAlign":"center","background":"url(http://codegen.caihongy.cn/20251118/2da4e59a1e2040a8b5726111ef573b48.png) no-repeat center / 100% 100%","flex":"none","display":"flex","width":"100%","justifyContent":"space-between","height":"auto"}'>
						<div :style='{"padding":"0 0 0 100px","color":"#fff","textAlign":"left","background":"none","fontSize":"16px","lineHeight":"40px","fontWeight":"600","height":"40px"}'>
							新能源资讯
							(浏览量(万)TOP20)
						</div>
					</div>
					<div id="autohomeTable" :style='{"width":"100%","fontSize":"14px","overflow":"hidden","flexWrap":"wrap","display":"flex","height":"calc(100% - 40px)"}'>
						<div :style='{"width":"23%","padding":"5px","margin":"0 auto","background":"none"}' v-for="(item,index) in autohomeList" :key="index">
							<img v-if="item.imgurl&&item.imgurl.substring(0,4)=='http'&&item.imgurl.split(',w').length>1" :src="item.imgurl" :style='{"width":"100%","objectFit":"cover","borderRadius":"4px","height":"100px"}'>
							<img v-else-if="item.imgurl&&item.imgurl.substring(0,4)=='http'" :src="item.imgurl.split(',')[0]" :style='{"width":"100%","objectFit":"cover","borderRadius":"4px","height":"100px"}'>
							<img v-else :src="$base.url+item.imgurl.split(',')[0]" :style='{"width":"100%","objectFit":"cover","borderRadius":"4px","height":"100px"}'>
							<div :style='{"color":"#fff"}'>{{item.title}}</div>
						</div>
					</div>
				</div>
			</div>
			<div :style='{"padding":"0","flexWrap":"wrap","flexDirection":"column","background":"none","display":"flex","gap":"10px","width":"25%"}'>
				<div class="echarts4">
					<div :style='{"padding":"0","margin":"0","textAlign":"center","background":"url(http://codegen.caihongy.cn/20251118/2da4e59a1e2040a8b5726111ef573b48.png) no-repeat center / 100% 100%","flex":"none","display":"flex","width":"100%","justifyContent":"space-between","height":"auto"}'>
						<div :style='{"padding":"0 0 0 50px","color":"#fff","textAlign":"left","background":"none","fontSize":"16px","lineHeight":"40px","fontWeight":"600","height":"40px"}'>
							行业资讯收藏量
						</div>
					</div>
					<div :style='{"width":"100%","flex":"auto","background":"url(http://codegen.caihongy.cn/20251118/073929b9a3bc4164b6e53f03896fc462.png) no-repeat center / 100% 100%","height":"0"}'>
						<div id="xingyezixunChart4" style="width:100%;height:100%;"></div>
					</div>
				</div>
				<div class="echarts5">
					<div :style='{"padding":"0","margin":"0","textAlign":"center","background":"url(http://codegen.caihongy.cn/20251118/2da4e59a1e2040a8b5726111ef573b48.png) no-repeat center / 100% 100%","flex":"none","display":"flex","width":"100%","justifyContent":"space-between","height":"auto"}'>
						<div :style='{"padding":"0 0 0 100px","color":"#fff","textAlign":"left","background":"none","fontSize":"16px","lineHeight":"40px","fontWeight":"600","height":"40px"}'>
							资讯分类
						</div>
					</div>
					<div :style='{"width":"100%","flex":"auto","background":"url(http://codegen.caihongy.cn/20251118/073929b9a3bc4164b6e53f03896fc462.png) no-repeat center / 100% 100%","height":"0"}'>
						<div id="xingyezixunChart5" style="width:100%;height:100%;"></div>
					</div>
				</div>
				<div class="echarts6">
					<div :style='{"padding":"0","margin":"0","textAlign":"center","background":"url(http://codegen.caihongy.cn/20251118/2da4e59a1e2040a8b5726111ef573b48.png) no-repeat center / 100% 100%","flex":"none","display":"flex","width":"100%","justifyContent":"space-between","height":"auto"}'>
						<div :style='{"padding":"0 0 0 100px","color":"#fff","textAlign":"left","background":"none","fontSize":"16px","lineHeight":"40px","fontWeight":"600","height":"40px"}'>
							日行业资讯发布量
						</div>
						<el-select
							v-if="changeStatQuery(['users'])"
							class="querySelect"
							v-model="xingyezixunchartQuery6.faburen" placeholder="请选择" @change="xingyezixunChat6" clearable>
							<el-option v-for="item in xingyezixunChartOptions6" :label="item" :value="item"></el-option>
						</el-select>
					</div>
					<div :style='{"width":"100%","flex":"auto","background":"url(http://codegen.caihongy.cn/20251118/073929b9a3bc4164b6e53f03896fc462.png) no-repeat center / 100% 100%","height":"0"}'>
						<div id="xingyezixunChart6" style="width:100%;height:100%;"></div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>
<script>
	import * as echarts from 'echarts'
	import chinaJson from "@/components/echarts/china.json";
	import router from '@/router/router-static'
	export default {
		data() {
			return {
				line: {"backgroundColor":"transparent","yAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":15,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#959aa5","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":120,"fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":false,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#666","shadowBlur":0,"width":1,"type":"dashed","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,0.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"xAxis":{"axisLabel":{"borderType":"solid","rotate":30,"padding":0,"shadowOffsetX":0,"margin":6,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#959aa5","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"truncate","borderRadius":0,"borderWidth":0,"width":120,"fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"color":["#42cc8a","#f48605","#d7b011","#fce74e","#80d6eb","#a896ef","#5366f6"],"legend":{"show":false},"grid":{"right":"20","top":"20","left":"20","bottom":"20","containLabel":true},"series":{"animationDuration":3000,"symbol":"circle","animationEasing":"backOut","showSymbol":true,"symbolSize":5,"itemStyle":{"color":"","borderColor":"rgba(66,204,138,0.3)","borderWidth":12},"animation":true},"tooltip":{"backgroundColor":"#123","trigger":"axis","textStyle":{"color":"#fff"}},"title":{"show":false}},
				line2: {"backgroundColor":"transparent","yAxis":{"axisLabel":{"borderType":"solid","rotate":30,"padding":0,"shadowOffsetX":0,"margin":6,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#959aa5","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"truncate","borderRadius":0,"borderWidth":0,"width":120,"fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":false,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#666","shadowBlur":0,"width":1,"type":"dashed","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,0.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"xAxis":{"axisLabel":{"borderType":"solid","rotate":30,"padding":0,"shadowOffsetX":0,"margin":6,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#959aa5","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"truncate","borderRadius":0,"borderWidth":0,"width":120,"fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"color":["#42cc8a","#f48605","#d7b011","#fce74e","#80d6eb","#a896ef","#5366f6"],"legend":{"show":false},"grid":{"right":"20","top":"20","left":"20","bottom":"20","containLabel":true},"series":{"animationDuration":3000,"symbol":"circle","animationEasing":"backOut","showSymbol":true,"symbolSize":5,"itemStyle":{"color":"","borderColor":"rgba(66,204,138,0.3)","borderWidth":12},"animation":true},"tooltip":{"backgroundColor":"#123","trigger":"axis","textStyle":{"color":"#fff"}},"title":{"show":false}},
				line3: {"backgroundColor":"transparent","yAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":15,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#959aa5","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":false,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#666","shadowBlur":0,"width":1,"type":"dashed","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,0.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"xAxis":{"axisLabel":{"borderType":"solid","rotate":30,"padding":0,"shadowOffsetX":0,"margin":6,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#959aa5","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"truncate","borderRadius":0,"borderWidth":0,"width":120,"fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"color":["#42cc8a","#f48605","#d7b011","#fce74e","#80d6eb","#a896ef","#5366f6"],"legend":{"show":false},"grid":{"right":"20","top":"20","left":"20","bottom":"20","containLabel":true},"series":{"animationDuration":6000,"symbol":"circle","animationEasing":"backOut","areaStyle":{"color":{"x":0,"y":0,"y2":1,"x2":0,"colorStops":[{"offset":0,"color":"rgba(66,204,138,0.5)"},{"offset":1,"color":"rgba(66,204,138,0)"}],"type":"linear"},"shadowBlur":10,"shadowColor":"rgba(0, 0, 0, 0.1)"},"showSymbol":true,"symbolSize":5,"itemStyle":{"color":"","borderColor":"rgba(84,112,198,0.3)","borderWidth":12},"animation":true},"tooltip":{"backgroundColor":"#123","trigger":"axis","textStyle":{"color":"#fff"}},"title":{"show":false}},
				line4: {"backgroundColor":"transparent","yAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":15,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#959aa5","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":false,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#666","shadowBlur":0,"width":1,"type":"dashed","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,0.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"xAxis":{"axisLabel":{"borderType":"solid","rotate":30,"padding":0,"shadowOffsetX":0,"margin":6,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#959aa5","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"truncate","borderRadius":0,"borderWidth":0,"width":120,"fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"color":["#42cc8a","#f48605","#d7b011","#fce74e","#80d6eb","#a896ef","#5366f6"],"legend":{"show":false},"grid":{"right":"20","top":"20","left":"20","bottom":"20","containLabel":true},"series":{"animationDuration":3000,"symbol":"circle","animationEasing":"backOut","areaStyle":{"color":{"x":0,"y":0,"y2":1,"x2":0,"colorStops":[{"offset":0,"color":"rgba(66,204,138,0.5)"},{"offset":1,"color":"rgba(66,204,138,0)"}],"type":"linear"},"shadowBlur":10,"shadowColor":"rgba(0, 0, 0, 0.1)"},"showSymbol":true,"symbolSize":5,"itemStyle":{"color":"","borderColor":"rgba(66,204,138,0.3)","borderWidth":12},"animation":true},"tooltip":{"backgroundColor":"#123","trigger":"axis","textStyle":{"color":"#fff"}},"title":{"show":false}},
				line5: {"backgroundColor":"transparent","yAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":15,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#959aa5","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":false,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#666","shadowBlur":0,"width":1,"type":"dashed","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,0.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"xAxis":{"axisLabel":{"borderType":"solid","rotate":30,"padding":0,"shadowOffsetX":0,"margin":6,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#959aa5","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"truncate","borderRadius":0,"borderWidth":0,"width":120,"fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"color":["#42cc8a","#f48605","#d7b011","#fce74e","#80d6eb","#a896ef","#5366f6"],"legend":{"shadowOffsetX":0,"borderColor":"#666","shadowOffsetY":0,"shadowBlur":0,"itemHeight":14,"show":true,"icon":"roundRect","type":"scroll","top":"top","lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"borderWidth":0,"itemWidth":20,"shadowColor":"rgba(0,0,0,.3)","height":"auto","padding":0,"itemGap":10,"backgroundColor":"transparent","orient":"horizontal","bottom":"auto","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"right":"auto","borderRadius":0,"left":"center","width":"80%","textStyle":{"textBorderWidth":0,"color":"#959aa5","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0}},"grid":{"right":"20","top":"40","left":"20","bottom":"20","containLabel":true},"series":{"animationDuration":6000,"symbol":"circle","animationEasing":"backOut","areaStyle":{"color":{"x":0,"y":0,"y2":1,"x2":0,"colorStops":[{"offset":0,"color":"rgba(0, 251, 255, 0)"},{"offset":1,"color":"rgba(0, 251, 255, 0)"}],"type":"linear"},"shadowBlur":10,"shadowColor":"rgba(0, 0, 0, 0.1)"},"showSymbol":true,"symbolSize":5,"itemStyle":{"color":"","borderColor":"rgba(84,112,198,0.3)","borderWidth":8},"animation":true},"series2":{"barWidth":"auto","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"#666","shadowOffsetY":0,"color":"","borderRadius":[0,0,0,0],"shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"#000"},"color":{"x":0,"y":0,"y2":1,"x2":0,"colorStops":[{"offset":0,"color":"rgba(100,253,255,1)"},{"offset":1,"color":"rgba(30,144,255,1)"}],"type":"linear"},"barCategoryGap":"20%"},"tooltip":{"backgroundColor":"#123","trigger":"axis","textStyle":{"color":"#fff"}},"title":{"show":false}},
				bar: {"backgroundColor":"transparent","yAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":12,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"color":"#959aa5","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#666","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#666","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,0.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"xAxis":{"axisLabel":{"borderType":"solid","rotate":30,"padding":0,"shadowOffsetX":0,"margin":6,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#959aa5","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"truncate","borderRadius":0,"borderWidth":0,"width":120,"fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":false,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"color":["#42cc8a","#f48605","#d7b011","#fce74e","#80d6eb","#a896ef","#5366f6"],"legend":{"padding":0,"itemGap":10,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"orient":"horizontal","shadowBlur":0,"bottom":"auto","itemHeight":14,"show":false,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"right":"auto","top":"bottom","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"center","borderWidth":0,"width":"80%","itemWidth":20,"textStyle":{"textBorderWidth":0,"color":"inherit","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":12,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"grid":{"right":"20","top":"20","left":"20","bottom":"20","containLabel":true},"series":{"animationDuration":3000,"itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"borderRadius":[0,0,0,0],"shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"animationEasing":"backOut","color":{"x":0,"y":0,"y2":1,"x2":0,"colorStops":[{"offset":0,"color":"rgba(100,253,255,1)"},{"offset":1,"color":"rgba(30,144,255,1)"}],"type":"linear"},"animation":true},"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"title":{"show":false},"base":{"animate":false,"interval":6000}},
				bar2: {"backgroundColor":"transparent","yAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":6,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#959aa5","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"truncate","borderRadius":0,"borderWidth":0,"width":120,"fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":true,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#666","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#666","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,0.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"xAxis":{"axisLabel":{"borderType":"solid","rotate":0,"padding":0,"shadowOffsetX":0,"margin":4,"backgroundColor":"transparent","borderColor":"#000","shadowOffsetY":0,"color":"#959aa5","shadowBlur":0,"show":true,"inside":false,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"width":"","fontSize":12,"lineHeight":24,"shadowColor":"transparent","fontWeight":"normal","height":""},"axisTick":{"show":false,"length":5,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"inside":false},"splitLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":false},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"cap":"butt","color":"#959aa5","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"rgba(0,0,0,.5)"},"show":true},"splitArea":{"show":false,"areaStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"rgba(25,25,25,.3)","opacity":1,"shadowBlur":10,"shadowColor":"rgba(0,0,0,.5)"}}},"color":["#42cc8a","#f48605","#d7b011","#fce74e","#80d6eb","#a896ef","#5366f6"],"legend":{"padding":0,"itemGap":10,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#666","shadowOffsetY":0,"orient":"horizontal","shadowBlur":0,"bottom":"auto","itemHeight":14,"show":false,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"right":"auto","top":"bottom","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"center","borderWidth":0,"width":"80%","itemWidth":20,"textStyle":{"textBorderWidth":0,"color":"inherit","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":12,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"grid":{"right":"20","top":"20","left":"20","bottom":"20","containLabel":true},"series":{"animationDuration":3000,"itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"borderRadius":[0,0,0,0],"shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"animationEasing":"backOut","color":{"x":0,"y":0,"y2":0,"x2":1,"colorStops":[{"offset":0,"color":"rgba(100,253,255,1)"},{"offset":1,"color":"rgba(30,144,255,1)"}],"type":"linear"},"animation":true},"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"title":{"show":false},"base":{"animate":true,"interval":2000}},
				bar3: {"polar":{"radius":[20,"80%"]},"backgroundColor":"transparent","radiusAxis":{"type":"category"},"color":["#42cc8a","#f48605","#d7b011","#fce74e","#80d6eb","#a896ef","#5366f6"],"legend":{"show":false},"series":{"barWidth":"auto","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"#fff","shadowOffsetY":0,"color":{"x":0,"y":0,"y2":1,"x2":0,"colorStops":[{"offset":0,"color":"rgba(100,253,255,1)"},{"offset":1,"color":"rgba(30,144,255,1)"}],"type":"linear"},"shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"#000"},"coordinateSystem":"polar","label":{"formatter":"{b}: {c}","show":true,"position":"middle"},"barCategoryGap":"20%"},"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"},"trigger":"axis"},"title":{"show":false},"base":{"animate":false,"interval":2000},"angleAxis":{"startAngle":90}},
				pie: {"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"backgroundColor":"transparent","color":["#42cc8a","#f48605","#d7b011","#fce74e","#80d6eb","#a896ef","#5366f6"],"title":{"show":false},"legend":{"shadowOffsetX":0,"borderColor":"#666","shadowOffsetY":0,"shadowBlur":0,"itemHeight":8,"show":true,"icon":"roundRect","type":"scroll","top":"bottom","lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"borderWidth":0,"itemWidth":16,"shadowColor":"rgba(0,0,0,.3)","height":"auto","padding":0,"itemGap":6,"backgroundColor":"transparent","orient":"horizontal","bottom":"auto","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"right":"auto","borderRadius":0,"left":"center","width":"100%","textStyle":{"textBorderWidth":0,"color":"#959aa5","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0}},"series":{"animationDuration":4000,"animationEasing":"quadraticOut","top":30,"left":30,"bottom":30,"itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"#666","shadowOffsetY":0,"color":"","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"#000"},"right":30,"label":{"borderType":"solid","rotate":0,"padding":0,"textBorderWidth":0,"backgroundColor":"transparent","borderColor":"#fff","color":"#fff","show":true,"textShadowColor":"transparent","distanceToLabelLine":5,"ellipsis":"...","formatter":"{d}%","overflow":"none","borderRadius":0,"borderWidth":0,"fontSize":12,"lineHeight":18,"textShadowOffsetX":0,"position":"inside","textShadowOffsetY":0,"textBorderType":"solid","textBorderColor":"#fff","textShadowBlur":0},"labelLine":{"show":true,"length":10,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"#fff","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"#000"},"length2":14,"smooth":false},"radius":[0,"75%"],"animation":true}},
				pie2: {"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"backgroundColor":"transparent","color":["#42cc8a","#f48605","#d7b011","#fce74e","#80d6eb","#a896ef","#5366f6"],"title":{"show":false},"legend":{"shadowOffsetX":0,"borderColor":"#666","shadowOffsetY":0,"shadowBlur":0,"itemHeight":8,"show":true,"icon":"roundRect","type":"scroll","top":"top","lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"borderWidth":0,"itemWidth":12,"shadowColor":"rgba(0,0,0,.3)","height":"auto","padding":0,"itemGap":4,"backgroundColor":"transparent","orient":"horizontal","bottom":"auto","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"right":"auto","borderRadius":0,"left":"center","width":"100%","textStyle":{"textBorderWidth":0,"color":"#959aa5","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0}},"series":{"animationDuration":4000,"animationEasing":"quadraticOut","avoidLabelOverlap":false,"itemStyle":{"borderRadius":10,"borderColor":"#111","borderWidth":2},"label":{"color":"inherit","show":false,"position":"outside"},"labelLine":{"show":false},"padAngle":10,"radius":["30%","75%"],"animation":true}},
				pie3: {"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"backgroundColor":"transparent","color":["#42cc8a","#f48605","#d7b011","#fce74e","#80d6eb","#a896ef","#5366f6"],"title":{"show":false},"legend":{"shadowOffsetX":0,"borderColor":"#666","shadowOffsetY":0,"shadowBlur":0,"itemHeight":8,"show":true,"icon":"roundRect","type":"scroll","top":"bottom","lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"borderWidth":0,"itemWidth":14,"shadowColor":"rgba(0,0,0,.3)","height":"auto","padding":0,"itemGap":10,"backgroundColor":"transparent","orient":"horizontal","bottom":"auto","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"right":"auto","borderRadius":0,"left":"center","width":"100%","textStyle":{"textBorderWidth":0,"color":"#959aa5","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0}},"series":{"itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"#111","shadowOffsetY":0,"color":"","borderRadius":5,"shadowBlur":0,"borderWidth":4,"opacity":1,"shadowColor":"#000"},"label":{"borderType":"solid","rotate":0,"padding":0,"textBorderWidth":0,"backgroundColor":"transparent","borderColor":"#fff","color":"#fff","show":true,"textShadowColor":"transparent","distanceToLabelLine":5,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"fontSize":12,"lineHeight":18,"textShadowOffsetX":0,"position":"outside","textShadowOffsetY":0,"textBorderType":"solid","textBorderColor":"#fff","textShadowBlur":0},"labelLine":{"show":true,"length":10,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"#fff","shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"#000"},"length2":14,"smooth":false},"radius":["20%","75%"]}},
				funnel: {"backgroundColor":"transparent","color":["#42cc8a","#f48605","#d7b011","#fce74e","#80d6eb","#a896ef","#5366f6"],"grid":{"right":"30","top":"30","left":"30","bottom":"30"},"legend":{"shadowOffsetX":0,"borderColor":"#666","shadowOffsetY":0,"shadowBlur":0,"itemHeight":8,"show":true,"icon":"roundRect","type":"scroll","top":"top","lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"borderWidth":0,"itemWidth":12,"shadowColor":"rgba(0,0,0,.3)","height":"auto","padding":0,"itemGap":4,"backgroundColor":"transparent","orient":"horizontal","bottom":"auto","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"right":"auto","borderRadius":0,"left":"center","width":"100%","textStyle":{"textBorderWidth":0,"color":"#959aa5","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0}},"series":{"itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"#000","shadowOffsetY":0,"color":"","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"#000"},"label":{"borderType":"solid","rotate":0,"padding":0,"textBorderWidth":0,"backgroundColor":"transparent","borderColor":"#fff","color":"","show":true,"textShadowColor":"transparent","distanceToLabelLine":5,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"fontSize":12,"lineHeight":18,"textShadowOffsetX":0,"position":"outside","textShadowOffsetY":0,"textBorderType":"solid","textBorderColor":"#fff","textShadowBlur":0},"labelLine":{"show":true,"length":10,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"#000"},"length2":14,"smooth":false},"gap":2},"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"title":{"show":false}},
				funnel2: {"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"backgroundColor":"transparent","color":["#42cc8a","#f48605","#d7b011","#fce74e","#80d6eb","#a896ef","#5366f6"],"title":{"show":false},"legend":{"padding":0,"itemGap":0,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#ccc","shadowOffsetY":0,"orient":"vertical","shadowBlur":0,"bottom":"auto","itemHeight":8,"show":true,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"top":"auto","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"left","borderWidth":0,"width":"auto","itemWidth":14,"textStyle":{"textBorderWidth":0,"color":"inherit","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":20,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"series":{"itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"#000","shadowOffsetY":0,"color":"","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"#000"},"label":{"borderType":"solid","rotate":0,"padding":0,"textBorderWidth":0,"backgroundColor":"transparent","borderColor":"#fff","color":"","show":true,"textShadowColor":"transparent","distanceToLabelLine":5,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"fontSize":12,"lineHeight":18,"textShadowOffsetX":0,"position":"outside","textShadowOffsetY":0,"textBorderType":"solid","textBorderColor":"#fff","textShadowBlur":0},"labelLine":{"show":true,"length":10,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"#000"},"length2":14,"smooth":false},"gap":2}},
				funnel3: {"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"backgroundColor":"transparent","color":["#42cc8a","#f48605","#d7b011","#fce74e","#80d6eb","#a896ef","#5366f6"],"title":{"show":false},"legend":{"padding":0,"itemGap":0,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#ccc","shadowOffsetY":0,"orient":"vertical","shadowBlur":0,"bottom":"auto","itemHeight":8,"show":true,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"top":"auto","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"left","borderWidth":0,"width":"auto","itemWidth":14,"textStyle":{"textBorderWidth":0,"color":"inherit","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":20,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"series":{"itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"#000","shadowOffsetY":0,"color":"","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"#000"},"label":{"borderType":"solid","rotate":0,"padding":0,"textBorderWidth":0,"backgroundColor":"transparent","borderColor":"#fff","color":"","show":true,"textShadowColor":"transparent","distanceToLabelLine":5,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"fontSize":12,"lineHeight":18,"textShadowOffsetX":0,"position":"outside","textShadowOffsetY":0,"textBorderType":"solid","textBorderColor":"#fff","textShadowBlur":0},"labelLine":{"show":true,"length":10,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"#000"},"length2":14,"smooth":false},"gap":2}},
				funnel4: {"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"backgroundColor":"transparent","color":["#42cc8a","#f48605","#d7b011","#fce74e","#80d6eb","#a896ef","#5366f6"],"title":{"show":false},"legend":{"padding":0,"itemGap":0,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#ccc","shadowOffsetY":0,"orient":"vertical","shadowBlur":0,"bottom":"auto","itemHeight":8,"show":true,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"top":"auto","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"left","borderWidth":0,"width":"auto","itemWidth":14,"textStyle":{"textBorderWidth":0,"color":"inherit","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":20,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"series":{"itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"#000","shadowOffsetY":0,"color":"","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"#000"},"label":{"borderType":"solid","rotate":0,"padding":0,"textBorderWidth":0,"backgroundColor":"transparent","borderColor":"#fff","color":"","show":true,"textShadowColor":"transparent","distanceToLabelLine":5,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"fontSize":12,"lineHeight":18,"textShadowOffsetX":0,"position":"outside","textShadowOffsetY":0,"textBorderType":"solid","textBorderColor":"#fff","textShadowBlur":0},"labelLine":{"show":true,"length":10,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"#000"},"length2":14,"smooth":false},"gap":2}},
				funnel5: {"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"backgroundColor":"transparent","color":["#42cc8a","#f48605","#d7b011","#fce74e","#80d6eb","#a896ef","#5366f6"],"title":{"show":false},"legend":{"padding":0,"itemGap":0,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#ccc","shadowOffsetY":0,"orient":"vertical","shadowBlur":0,"bottom":"auto","itemHeight":8,"show":true,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"top":"auto","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"left","borderWidth":0,"width":"auto","itemWidth":14,"textStyle":{"textBorderWidth":0,"color":"inherit","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":20,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"series":{"itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"#000","shadowOffsetY":0,"color":"","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"#000"},"label":{"borderType":"solid","rotate":0,"padding":0,"textBorderWidth":0,"backgroundColor":"transparent","borderColor":"#fff","color":"","show":true,"textShadowColor":"transparent","distanceToLabelLine":5,"ellipsis":"...","overflow":"none","borderRadius":0,"borderWidth":0,"fontSize":12,"lineHeight":18,"textShadowOffsetX":0,"position":"outside","textShadowOffsetY":0,"textBorderType":"solid","textBorderColor":"#fff","textShadowBlur":0},"labelLine":{"show":true,"length":10,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"shadowBlur":0,"width":1,"type":"solid","opacity":1,"shadowColor":"#000"},"length2":14,"smooth":false},"gap":2}},
				map: {"tooltip":{"formatter":"{b} : {c}","trigger":"item"},"backgroundColor":"transparent","title":{"borderType":"solid","padding":10,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#ccc","shadowOffsetY":0,"shadowBlur":0,"bottom":"auto","show":true,"right":"auto","top":"auto","borderRadius":0,"left":"left","borderWidth":0,"textStyle":{"textBorderWidth":0,"color":"#fff","textShadowColor":"transparent","fontSize":14,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"#ccc","textShadowBlur":0},"shadowColor":"transparent"},"legend":{"padding":5,"itemGap":10,"shadowOffsetX":0,"backgroundColor":"transparent","borderColor":"#ccc","shadowOffsetY":0,"orient":"horizontal","shadowBlur":0,"bottom":"auto","itemHeight":14,"show":false,"icon":"roundRect","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"right":"auto","top":"auto","borderRadius":0,"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"left":"right","borderWidth":0,"width":"auto","itemWidth":25,"textStyle":{"textBorderWidth":0,"color":"#fff","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0},"shadowColor":"rgba(0,0,0,.3)","height":"auto"},"series":{"aspectScale":0.75,"itemStyle":{"areaColor":"#a8d5fc"},"zoom":1.8,"label":{"emphasis":{"show":true,"textStyle":{"color":"#3ba372"}},"normal":{"color":"#3ba372","show":true}},"roam":true,"showLegendSymbol":false,"animation":false},"visualMap":{"min":0,"text":["High","Low"],"inRange":{"color":["#358aff","#39d3f9","#f2993d","#fce74e","#80d6eb","#a896ef","#5366f6","rgba(30, 144, 255, 1)","rgba(0, 251, 255, 1)","rgba(255, 120, 0, 1)","#f9d354","#e3faf7","#3c8883","#dda882"]},"max":80000,"calculable":true,"seriesIndex":[0]}},
				boardBase: {"funnelNum":8,"lineNum":10,"radarNum":8,"gaugeNum":8,"barNum":10,"pieNum":10},
				gauge: {"tooltip":{"formatter":"{b} : {c}","trigger":"item"},"backgroundColor":"transparent","color":["#42cc8a","#f48605","#d7b011","#fce74e","#80d6eb","#a896ef","#5366f6"],"title":{"show":false},"series":{"pointer":{"offsetCenter":[0,"10%"],"icon":"path://M2.9,0.7L2.9,0.7c1.4,0,2.6,1.2,2.6,2.6v115c0,1.4-1.2,2.6-2.6,2.6l0,0c-1.4,0-2.6-1.2-2.6-2.6V3.3C0.3,1.9,1.4,0.7,2.9,0.7z","width":8,"length":"80%"},"axisLine":{"lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"opacity":0.5,"shadowBlur":1,"shadowColor":"#000"},"roundCap":true},"anchor":{"show":true,"itemStyle":{"color":"inherit"},"size":18,"showAbove":true},"emphasis":{"disabled":false},"progress":{"show":true,"roundCap":true,"overlap":true},"splitNumber":10,"detail":{"formatter":"{value}","backgroundColor":"inherit","color":"#fff","borderRadius":3,"width":20,"fontSize":12,"height":12},"title":{"color":"#ccc","fontSize":12},"animation":true}},
				radar: {"backgroundColor":"transparent","radar":{"splitLine":{"lineStyle":{"color":"rgba(255, 255, 255, 0.1)"}},"name":{"textStyle":{"color":"#ddd","fontSize":13,"fontWeight":"bold"}},"shape":"circle","axisLine":{"lineStyle":{"color":"rgba(255, 255, 255, 0.2)"}},"splitArea":{"areaStyle":{"color":["rgba(0, 0, 0, 0.1)","rgba(20, 20, 20, 0.1)"],"opacity":1}}},"color":["#42cc8a","#f48605","#d7b011","#fce74e","#80d6eb","#a896ef","#5366f6"],"legend":{"shadowOffsetX":0,"borderColor":"#ccc","shadowOffsetY":0,"shadowBlur":0,"itemHeight":14,"show":true,"icon":"roundRect","type":"scroll","top":"auto","lineStyle":{"shadowOffsetX":0,"shadowOffsetY":0,"color":"inherit","shadowBlur":0,"width":"auto","type":"inherit","opacity":1,"shadowColor":"transparent"},"borderWidth":0,"itemWidth":25,"shadowColor":"rgba(0,0,0,.3)","height":"auto","padding":5,"itemGap":10,"backgroundColor":"transparent","orient":"horizontal","bottom":"auto","itemStyle":{"borderType":"solid","shadowOffsetX":0,"borderColor":"inherit","shadowOffsetY":0,"color":"inherit","shadowBlur":0,"borderWidth":0,"opacity":1,"shadowColor":"transparent"},"right":"auto","borderRadius":0,"left":"right","width":"auto","textStyle":{"textBorderWidth":0,"color":"#fff","textShadowColor":"transparent","ellipsis":"...","overflow":"none","fontSize":12,"lineHeight":24,"textShadowOffsetX":0,"textShadowOffsetY":0,"textBorderType":"solid","fontWeight":500,"textBorderColor":"transparent","textShadowBlur":0}},"series":{},"tooltip":{"backgroundColor":"#123","textStyle":{"color":"#fff"}},"title":{"top":"bottom","show":false,"left":"left"}},
				myChart0: null,
				myChartIntervalTimers: {},
				autohomeList: [],
				autohomeTimer: null,
				dates: '',
				autohomeCount: 0,
				xingyezixunCount: 0,
				frontType: 0,
				autohomechartQuery1: {},
				autohomeChartOptions1: [],
				autohomechartQuery2: {},
				autohomeChartOptions2: [],
				xingyezixunchartQuery3: {},
				xingyezixunChartOptions3: [],
				xingyezixunchartQuery4: {},
				xingyezixunChartOptions4: [],
				xingyezixunchartQuery5: {},
				xingyezixunChartOptions5: [],
				xingyezixunchartQuery6: {},
				xingyezixunChartOptions6: [],
			};
		},
		mounted(){
			if(this.$route.query.frontType&&this.$route.query.frontType==1) {
				this.frontType = 1
			}
			this.init();
			this.getautohomeList()
		},
		beforeDestroy() {
			Object.keys(this.myChartIntervalTimers).forEach((key) => {
				const id = this.myChartIntervalTimers[key]
				if (id) clearInterval(id)
			})
			this.myChartIntervalTimers = {}
			if (this.sxairqualityTimer) clearInterval(this.sxairqualityTimer)
		},
		computed: {
			sessionForm() {
				return JSON.parse(this.$storage.getObj('userForm'))
			},
		},
		created() {
			this.$nextTick(()=>{
				this.times()
				setTimeout(()=>{
					this.getautohomeCount();
					this.autohomeChat1();
					this.autohomeChat2();
					this.getxingyezixunCount();
					this.xingyezixunChat3();
					this.xingyezixunChat4();
					this.xingyezixunChat5();
					this.getxingyezixunfaburenOptions6()
					this.xingyezixunChat6();
				},500)
			})
		},
		methods:{
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
			getautohomeList() {
				let params = {
					page: 1,
					limit: 20,
				}
				params.order = 'desc'
				params.sort = 'liulan'
				this.$http({
					url: "autohome/page",
					method: "get",
					params: params
				}).then(({ data }) => {
					if (data && data.code === 0) {
						this.autohomeList = data.data.list;
						let div = document.getElementById('autohomeTable')
						var scrollTop = -1
						function move() {
							if (div){
								if(div.scrollTop==scrollTop){
									div.scrollTo({
										top: 0, 
										behavior: "smooth"
									});
									return false
								}
								scrollTop = div.scrollTop
								div.scrollTo({ 
									top: div.scrollTop + 40, 
									behavior: "smooth"
								});
							}
								
						}
						this.autohomeTimer = setInterval(move, 2000);
						div.addEventListener('mouseenter', e => {
							e.stopPropagation()
							clearInterval(this.autohomeTimer);
						})
						div.addEventListener('mouseleave', e => {
							e.stopPropagation()
							this.autohomeTimer = setInterval(move, 2000);
						})
					}
				});
			},
			backClick(){
				if(this.frontType==1) {
					window.location.href = `${this.$base.indexUrl}`
					return false
				}
				this.$router.replace({ path: "/" });
			},
			myChartInterval(type, xAxisData, seriesData, myChart, timerKey) {
				if (timerKey && this.myChartIntervalTimers[timerKey]) {
					clearInterval(this.myChartIntervalTimers[timerKey])
					this.myChartIntervalTimers[timerKey] = null
				}
				this.$nextTick(() => {
					const intervalId = setInterval(() => {
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
					}, 6000)
					if (timerKey) {
						this.myChartIntervalTimers[timerKey] = intervalId
					}
				})
			},
			wordclouds(wordcloudData,echartsId) {
				let wordcloud = {"maskImage":"data:image/png;base64,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","option":{"tooltip":{"show":false},"backgroundColor":"transparent","series":[{"sizeRange":[9,32],"layoutAnimation":true,"shape":"circle","data":[{"name":"花鸟市场","value":1446},{"name":"汽车","value":928},{"name":"视频","value":906},{"name":"电视","value":825},{"name":"Lover Boy 88","value":514},{"name":"动漫","value":486},{"name":"音乐","value":53},{"name":"直播","value":163},{"name":"广播电台","value":86},{"name":"戏曲曲艺","value":17},{"name":"演出票务","value":6},{"name":"给陌生的你听","value":1},{"name":"资讯","value":1437},{"name":"商业财经","value":422},{"name":"娱乐八卦","value":353},{"name":"军事","value":331},{"name":"科技资讯","value":313},{"name":"社会时政","value":307},{"name":"时尚","value":43},{"name":"网络奇闻","value":15},{"name":"旅游出行","value":438},{"name":"景点类型","value":957},{"name":"国内游","value":927},{"name":"远途出行方式","value":908},{"name":"酒店","value":693},{"name":"关注景点","value":611},{"name":"旅游网站偏好","value":512},{"name":"出国游","value":382},{"name":"交通票务","value":312},{"name":"旅游方式","value":187},{"name":"旅游主题","value":163},{"name":"港澳台","value":104},{"name":"本地周边游","value":3},{"name":"小卖家","value":1331},{"name":"全日制学校","value":941},{"name":"基础教育科目","value":585},{"name":"考试培训","value":473},{"name":"语言学习","value":358},{"name":"留学","value":246},{"name":"K12课程培训","value":207},{"name":"艺术培训","value":194},{"name":"技能培训","value":104},{"name":"IT培训","value":87},{"name":"高等教育专业","value":63},{"name":"家教","value":48},{"name":"体育培训","value":23},{"name":"职场培训","value":5},{"name":"金融财经","value":1328},{"name":"银行","value":765},{"name":"股票","value":452},{"name":"保险","value":415},{"name":"贷款","value":253},{"name":"基金","value":211},{"name":"信用卡","value":180},{"name":"外汇","value":138},{"name":"P2P","value":116},{"name":"贵金属","value":98},{"name":"债券","value":93},{"name":"网络理财","value":92},{"name":"信托","value":90},{"name":"征信","value":76},{"name":"期货","value":76},{"name":"公积金","value":40},{"name":"银行理财","value":36},{"name":"银行业务","value":30},{"name":"典当","value":7},{"name":"海外置业","value":1},{"name":"汽车","value":1309},{"name":"汽车档次","value":965},{"name":"汽车品牌","value":900},{"name":"汽车车型","value":727},{"name":"购车阶段","value":461},{"name":"二手车","value":309},{"name":"汽车美容","value":260},{"name":"新能源汽车","value":173},{"name":"汽车维修","value":155},{"name":"租车服务","value":136},{"name":"车展","value":121},{"name":"违章查询","value":76},{"name":"汽车改装","value":62},{"name":"汽车用品","value":37},{"name":"路况查询","value":32},{"name":"汽车保险","value":28},{"name":"陪驾代驾","value":4},{"name":"网络购物","value":1275},{"name":"做我的猫","value":1088},{"name":"只想要你知道","value":907},{"name":"团购","value":837},{"name":"比价","value":201},{"name":"海淘","value":195},{"name":"移动APP购物","value":179},{"name":"支付方式","value":119},{"name":"代购","value":43},{"name":"体育健身","value":1234},{"name":"体育赛事项目","value":802},{"name":"运动项目","value":405},{"name":"体育类赛事","value":337},{"name":"健身项目","value":199},{"name":"健身房健身","value":78},{"name":"运动健身","value":77},{"name":"家庭健身","value":36},{"name":"健身器械","value":29},{"name":"办公室健身","value":3},{"name":"商务服务","value":1201},{"name":"法律咨询","value":508},{"name":"化工材料","value":147},{"name":"广告服务","value":125},{"name":"会计审计","value":115},{"name":"人员招聘","value":101},{"name":"印刷打印","value":66},{"name":"知识产权","value":32},{"name":"翻译","value":22},{"name":"安全安保","value":9},{"name":"公关服务","value":8},{"name":"商旅服务","value":2},{"name":"展会服务","value":2},{"name":"特许经营","value":1},{"name":"休闲爱好","value":1169},{"name":"收藏","value":412},{"name":"摄影","value":393},{"name":"温泉","value":230},{"name":"博彩彩票","value":211},{"name":"美术","value":207},{"name":"书法","value":139},{"name":"DIY手工","value":75},{"name":"舞蹈","value":23},{"name":"钓鱼","value":21},{"name":"棋牌桌游","value":17},{"name":"KTV","value":6},{"name":"密室","value":5},{"name":"采摘","value":4},{"name":"电玩","value":1},{"name":"真人CS","value":1},{"name":"轰趴","value":1},{"name":"家电数码","value":1111},{"name":"手机","value":885},{"name":"电脑","value":543},{"name":"大家电","value":321},{"name":"家电关注品牌","value":253},{"name":"网络设备","value":162},{"name":"摄影器材","value":149},{"name":"影音设备","value":133},{"name":"办公数码设备","value":113},{"name":"生活电器","value":67},{"name":"厨房电器","value":54},{"name":"智能设备","value":45},{"name":"个人护理电器","value":22},{"name":"服饰鞋包","value":1047},{"name":"服装","value":566},{"name":"饰品","value":289},{"name":"鞋","value":184},{"name":"箱包","value":168},{"name":"奢侈品","value":137},{"name":"母婴亲子","value":1041},{"name":"孕婴保健","value":505},{"name":"母婴社区","value":299},{"name":"早教","value":103},{"name":"奶粉辅食","value":66},{"name":"童车童床","value":41},{"name":"关注品牌","value":271},{"name":"宝宝玩乐","value":30},{"name":"母婴护理服务","value":25},{"name":"纸尿裤湿巾","value":16},{"name":"妈妈用品","value":15},{"name":"宝宝起名","value":12},{"name":"童装童鞋","value":9},{"name":"胎教","value":8},{"name":"宝宝安全","value":1},{"name":"宝宝洗护用品","value":1},{"name":"软件应用","value":1018},{"name":"系统工具","value":896},{"name":"理财购物","value":440},{"name":"生活实用","value":365},{"name":"影音图像","value":256},{"name":"社交通讯","value":214},{"name":"手机美化","value":39},{"name":"办公学习","value":28},{"name":"应用市场","value":23},{"name":"母婴育儿","value":14},{"name":"游戏","value":946},{"name":"手机游戏","value":565},{"name":"PC游戏","value":353},{"name":"网页游戏","value":254},{"name":"游戏机","value":188},{"name":"模拟辅助","value":166},{"name":"个护美容","value":942},{"name":"护肤品","value":177},{"name":"彩妆","value":133},{"name":"美发","value":80},{"name":"香水","value":50},{"name":"个人护理","value":46},{"name":"美甲","value":26},{"name":"SPA美体","value":21},{"name":"花鸟萌宠","value":914},{"name":"绿植花卉","value":311},{"name":"狗","value":257},{"name":"其他宠物","value":131},{"name":"水族","value":125},{"name":"猫","value":122},{"name":"动物","value":81},{"name":"鸟","value":67},{"name":"宠物用品","value":41},{"name":"宠物服务","value":26},{"name":"书籍阅读","value":913},{"name":"网络小说","value":483},{"name":"关注书籍","value":128},{"name":"文学","value":105},{"name":"报刊杂志","value":77},{"name":"人文社科","value":22},{"name":"建材家居","value":907},{"name":"装修建材","value":644},{"name":"家具","value":273},{"name":"家居风格","value":187},{"name":"家居家装关注品牌","value":140},{"name":"家纺","value":107},{"name":"厨具","value":47},{"name":"灯具","value":43},{"name":"家居饰品","value":29},{"name":"家居日常用品","value":10},{"name":"生活服务","value":883},{"name":"物流配送","value":536},{"name":"家政服务","value":108},{"name":"摄影服务","value":49},{"name":"搬家服务","value":38},{"name":"物业维修","value":37},{"name":"婚庆服务","value":24},{"name":"二手回收","value":24},{"name":"鲜花配送","value":3},{"name":"维修服务","value":3},{"name":"殡葬服务","value":1},{"name":"求职创业","value":874},{"name":"创业","value":363},{"name":"目标职位","value":162},{"name":"目标行业","value":50},{"name":"兼职","value":21},{"name":"期望年薪","value":20},{"name":"实习","value":16},{"name":"雇主类型","value":10},{"name":"星座运势","value":789},{"name":"星座","value":316},{"name":"算命","value":303},{"name":"解梦","value":196},{"name":"风水","value":93},{"name":"面相分析","value":47},{"name":"手相","value":32},{"name":"公益","value":90}],"keepAspect":false,"type":"wordCloud","rotationRange":[-90,90],"gridSize":8,"shrinkToFit":false,"top":"center","left":"center","width":"80%","emphasis":{"focus":"self","textStyle":{"textShadowColor":"#333","textShadowBlur":4}},"drawOutOfBound":false,"rotationStep":45,"textStyle":{"color":"function(){return\"rgb(\"+[Math.round(Math.floor(Math.random() * (100 - 255)) + 255),Math.round(Math.floor(Math.random() * (100 - 255)) + 255),Math.round(Math.floor(Math.random() * (100 - 255)) + 255)].join(\",\")+\")\"}","fontWeight":500,"fontFamily":"sans-serif"},"height":"80%","maskImage":{}}]}}
				wordcloud = JSON.parse(JSON.stringify(wordcloud), (k, v) => {
					if(typeof v == 'string' && v.indexOf('function') > -1){
						return eval("(function(){return "+v+" })()")
					}
					return v;
				})
				wordcloud.option.series[0].data=wordcloudData;
				
				this.myChart0 = echarts.init(document.getElementById(echartsId));
				let myChart = this.myChart0
				let img = wordcloud.maskImage
			
				if (img) {
					var maskImage = new Image();
					maskImage.src = img
					maskImage.onload = function() {
						wordcloud.option.series[0].maskImage = maskImage
						myChart.clear()
						myChart.setOption(wordcloud.option)
					}
				} else {
					delete wordcloud.option.series[0].maskImage
					myChart.clear()
					myChart.setOption(wordcloud.option)
				}
			},
			getTimeStrToDay(game_over_timestamp) {
				if (game_over_timestamp == 0)
					return "";
				var date = new Date(parseInt(game_over_timestamp));
				var now = new Date();
				var hours = date.getHours() >= 10 ? date.getHours().toString() : "0" + date.getHours();
				var minutes = date.getMinutes() >= 10 ? date.getMinutes().toString() : "0" + date.getMinutes();
				var seconds = date.getSeconds() >= 10 ? date.getSeconds().toString() : "0" + date.getSeconds();
				let arr = ["日", "一", "二", "三", "四", "五", "六"];
				let d = arr[date.getDay()]
				return date.getFullYear() + "年" + (date.getMonth() + 1) + "月" + date.getDate() + '日' + ' ' + ' ' + '星期' + d  + ' ' + "  " + hours + ":" + minutes + ":" + seconds
			},
			times() {
				setInterval(()=>{
					let date = new Date().getTime()
					this.dates = this.getTimeStrToDay(date)
				}, 1000)
			},
			filterTime(time) {
				const date = new Date(time)
				const Y = date.getFullYear()
				const M = date.getMonth() + 1 < 10 ? '0'+(date.getMonth()+1) : date.getMonth()+1 
				const D = date.getDate() < 10 ? '0' + date.getDate() : date.getDate()
			  
				const H = date.getHours() < 10 ? '0' + date.getHours() : date.getHours() // 小时
				const I = date.getMinutes() < 10 ? '0' + date.getMinutes() : date.getMinutes() // 分钟
				const S = date.getSeconds() < 10 ? '0' + date.getSeconds() : date.getSeconds() // 秒
			  
				return `${Y}-${M}-${D} ${H}:${I}:${S}`
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
			//统计接口1
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
							let res = data.data;
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
							
							let xAxisObj = this.line.xAxis
							xAxisObj.type = 'category'
							xAxisObj.boundaryGap = false
							xAxisObj.data = xAxis
							
							
							let yAxisObj = this.line.yAxis
							yAxisObj.type = 'value'
							
							let seriesObj = {
								data: yAxis,
								type: 'line',
							}
							seriesObj = Object.assign(seriesObj , this.line.series)
							const gridObj = this.line.grid
							let tooltipObj = {
								trigger: 'item',
								formatter: '{b} : {c}'
							}
							tooltipObj = Object.assign(tooltipObj , this.line.tooltip?this.line.tooltip:{})
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
							window.addEventListener('resize', () => {
								autohomeChart1.resize();
							},false);
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
			//统计接口2
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
							let res = data.data;
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
							let tooltipObj = {
								trigger: 'item',
								formatter: '{b} : {c} ({d}%)'
							}
							tooltipObj = Object.assign(tooltipObj , this.pie.tooltip?this.pie.tooltip:{})
							option = {
								backgroundColor: this.pie.backgroundColor,
								color: this.pie.color,
								title: titleObj,
								legend: legendObj,
								grid: gridObj,
								tooltip: tooltipObj,
								series: [seriesObj]
							};
							// 使用刚指定的配置项和数据显示图表。
							autohomeChart2.setOption(option);
				

							//根据窗口的大小变动图表
							window.addEventListener('resize', () => {
								autohomeChart2.resize();
							},false);
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
			//统计接口1
			xingyezixunChat3(e=null) {
				this.$nextTick(()=>{

					var xingyezixunChart3 = echarts.init(document.getElementById("xingyezixunChart3"),'macarons');
					let params = {
					}
					this.$http({
						url: `xingyezixun/value/zixunbiaoti/clicknum`,
						method: "get",
						params
					}).then(({ data }) => {
						if (data && data.code === 0) {
							let res = data.data;
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
							
							let xAxisObj = this.bar.xAxis
							xAxisObj.type = 'category'
							xAxisObj.data = xAxis
							
							
							let yAxisObj = this.bar.yAxis
							yAxisObj.type = 'value'
							
							let seriesObj = {
								data: yAxis,
								type: 'bar'
							}
							seriesObj = Object.assign(seriesObj , this.bar.series)
							const gridObj = this.bar.grid
							let tooltipObj = {
								trigger: 'item',
								formatter: '{b} : {c}'
							}
							tooltipObj = Object.assign(tooltipObj , this.bar.tooltip?this.bar.tooltip:{})
							option = {
								backgroundColor: this.bar.backgroundColor,
								color: this.bar.color,
								title: titleObj,
								legend: legendObj,
								tooltip: tooltipObj,
								xAxis: xAxisObj,
								yAxis: yAxisObj,
								grid: gridObj,
								series: [seriesObj]
							};
							// 使用刚指定的配置项和数据显示图表。
							xingyezixunChart3.setOption(option);
				

							//根据窗口的大小变动图表
							window.addEventListener('resize', () => {
								xingyezixunChart3.resize();
							},false);
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
			//统计接口2
			xingyezixunChat4(e=null) {
				this.$nextTick(()=>{

					var xingyezixunChart4 = echarts.init(document.getElementById("xingyezixunChart4"),'macarons');
					let params = {
					}
					this.$http({
						url: `xingyezixun/value/zixunbiaoti/storeupnum`,
						method: "get",
						params
					}).then(({ data }) => {
						if (data && data.code === 0) {
							let res = data.data;
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
							let tooltipObj = {
								trigger: 'item',
								formatter: "{b} : {c}"
							}
							tooltipObj = Object.assign(tooltipObj , this.funnel.tooltip?this.funnel.tooltip:{})
							option = {
								backgroundColor: this.funnel.backgroundColor,
								color: this.funnel.color,
								title: titleObj,
								legend: legendObj,
								tooltip: tooltipObj,
								grid: gridObj,
								series: seriesObj,
							}
							// 使用刚指定的配置项和数据显示图表。
							xingyezixunChart4.setOption(option);
				

							//根据窗口的大小变动图表
							window.addEventListener('resize', () => {
								xingyezixunChart4.resize();
							},false);
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
			//统计接口3
			xingyezixunChat5(e=null) {
				this.$nextTick(()=>{

					var xingyezixunChart5 = echarts.init(document.getElementById("xingyezixunChart5"),'macarons');
					let params = {
					}
					this.$http({
						url: "xingyezixun/group/zixunfenlei",
						method: "get",
						params
					}).then(({ data }) => {
						if (data && data.code === 0) {
							let res = data.data;
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
							let titleObj = this.pie3.title
							titleObj.text = '资讯分类'
							
							const legendObj = this.pie3.legend
							
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
							seriesObj = Object.assign(seriesObj , this.pie3.series)
							const gridObj = this.pie3.grid
							let tooltipObj = {
								trigger: 'item',
								formatter: '{b} : {c} ({d}%)'
							}
							tooltipObj = Object.assign(tooltipObj , this.pie3.tooltip?this.pie3.tooltip:{})
							option = {
								backgroundColor: this.pie3.backgroundColor,
								color: this.pie3.color,
								title: titleObj,
								legend: legendObj,
								tooltip: tooltipObj,
								grid: gridObj,
								series: [seriesObj]
							};
							// 使用刚指定的配置项和数据显示图表。
							xingyezixunChart5.setOption(option);
				

							//根据窗口的大小变动图表
							window.addEventListener('resize', () => {
								xingyezixunChart5.resize();
							},false);
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
			getxingyezixunfaburenOptions6() {
				this.$http.get('option/xingyezixun/faburen',
				).then(rs=>{
					this.xingyezixunChartOptions6 = rs.data.data
				})
			},
			//统计接口4
			xingyezixunChat6(e=null) {
				this.$nextTick(()=>{

					var xingyezixunChart6 = echarts.init(document.getElementById("xingyezixunChart6"),'macarons');
					let params = {
					}
					if(this.xingyezixunchartQuery6.faburen) {
						params.conditionColumn = 'faburen'
						params.conditionValue = this.xingyezixunchartQuery6.faburen
					}
					this.$http({
						url: "xingyezixun/group/fabushijian",
						method: "get",
						params
					}).then(({ data }) => {
						if (data && data.code === 0) {
							let res = data.data;
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
							let tooltipObj = {
								trigger: 'item',
								formatter: '{b} : {c} ({d}%)'
							}
							tooltipObj = Object.assign(tooltipObj , this.pie.tooltip?this.pie.tooltip:{})
							option = {
								backgroundColor: this.pie.backgroundColor,
								color: this.pie.color,
								title: titleObj,
								legend: legendObj,
								tooltip: tooltipObj,
								grid: gridObj,
								series: [seriesObj]
							};
							// 使用刚指定的配置项和数据显示图表。
							xingyezixunChart6.setOption(option);
				

							//根据窗口的大小变动图表
							window.addEventListener('resize', () => {
								xingyezixunChart6.resize();
							},false);
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
	// table
	.el-table:before{
		display: none;
	}
	.el-table:after{
		display: none;
	}
	.el-table ::v-deep .el-table__header-wrapper thead {
				color: #fff;
				font-weight: 500;
				width: 100%;
			}
	
	.el-table ::v-deep .el-table__header-wrapper thead tr {
				background: none;
			}
	
	.el-table ::v-deep .el-table__header-wrapper thead tr th {
				padding: 6px 0;
				background: none;
				border-color: #03bbff4d;
				border-width: 0 1px 1px 0;
				border-style: solid;
				text-align: left;
			}
	
	.el-table ::v-deep .el-table__header-wrapper thead tr th .cell {
				padding: 0 10px;
				word-wrap: normal;
				word-break: break-all;
				white-space: normal;
				font-weight: bold;
				display: inline-block;
				vertical-align: middle;
				width: 100%;
				line-height: 24px;
				position: relative;
				text-overflow: ellipsis;
			}
	
	.el-table ::v-deep .el-table__body-wrapper tbody {
				width: 100%;
			}
	
	.el-table ::v-deep .el-table__body-wrapper tbody tr {
				background: none;
			}
	
	.el-table ::v-deep .el-table__body-wrapper tbody tr td {
				padding: 6px 0;
				color: #fff;
				background: none;
				border-color: #03bbff4d;
				border-width: 0 1px 1px 0;
				border-style: solid;
				text-align: left;
			}
	
	
	.el-table ::v-deep .el-table__body-wrapper tbody tr:hover td {
				padding: 6px 0;
				color: #fff;
				background: none;
				border-color: #03bbff4d;
				border-width: 0 1px 1px 0;
				border-style: solid;
				text-align: left;
			}
	
	.el-table ::v-deep .el-table__body-wrapper tbody tr td {
				padding: 6px 0;
				color: #fff;
				background: none;
				border-color: #03bbff4d;
				border-width: 0 1px 1px 0;
				border-style: solid;
				text-align: left;
			}
	
	.el-table ::v-deep .el-table__body-wrapper tbody tr td .cell {
				padding: 0 10px;
				overflow: hidden;
				word-break: break-all;
				white-space: normal;
				line-height: 24px;
				text-overflow: ellipsis;
			}
	.echarts1 {
				padding: 8px 0 0 0;
				margin: 0;
				flex-direction: column;
				background: none;
				flex: auto;
				display: flex;
				width: 100%;
				transition: 0.3s;
				height: 0;
				::v-deep.querySelect {
			.el-input {
				height: auto
			}
			.el-input__inner,.el-range-input  {
								border: 1px solid #ffffff20;
								padding: 0 5px;
								margin: 5px auto 0 10px;
								z-index: 9;
								color: #fff;
								background: none;
								width: 90%;
								height: 32px;
							}
			.el-input__icon {
				line-height: 1;
			}
		}
		::v-deep.querySelect2 {
						border: 1px solid #ffffff20;
						padding: 0 5px;
						margin: 5px auto 0 10px;
						z-index: 9;
						color: #fff;
						background: none;
						width: 90%;
						height: 32px;
						.el-range-input  {
				background: none;
			}
			.el-input__icon {
				line-height: 1;
			}
		}
	}
	.echarts1:hover {
			}
	.echarts2 {
				padding: 8px 0 0 0;
				margin: 0;
				flex-direction: column;
				background: none;
				flex: auto;
				display: flex;
				width: 100%;
				transition: 0.3s;
				height: 0;
				::v-deep.querySelect {
			.el-input {
				height: auto
			}
			.el-input__inner,.el-range-input  {
								border: 1px solid #ffffff20;
								padding: 0 5px;
								margin: 5px auto 0 10px;
								z-index: 9;
								color: #fff;
								background: none;
								width: 90%;
								height: 32px;
							}
			.el-input__icon {
				line-height: 1;
			}
		}
		::v-deep.querySelect2 {
						border: 1px solid #ffffff20;
						padding: 0 5px;
						margin: 5px auto 0 10px;
						z-index: 9;
						color: #fff;
						background: none;
						width: 90%;
						height: 32px;
						.el-range-input  {
				background: none;
			}
			.el-input__icon {
				line-height: 1;
			}
		}
	}
	.echarts2:hover {
			}
	.echarts3 {
				padding: 8px 0 0 0;
				margin: 0;
				flex-direction: column;
				background: none;
				flex: auto;
				display: flex;
				width: 100%;
				transition: 0.3s;
				height: 0;
				::v-deep.querySelect {
			.el-input {
				height: auto
			}
			.el-input__inner,.el-range-input  {
								border: 1px solid #ffffff20;
								padding: 0 5px;
								margin: 5px auto 0 10px;
								z-index: 9;
								color: #fff;
								background: none;
								width: 90%;
								height: 32px;
							}
			.el-input__icon {
				line-height: 1;
			}
		}
		::v-deep.querySelect2 {
						border: 1px solid #ffffff20;
						padding: 0 5px;
						margin: 5px auto 0 10px;
						z-index: 9;
						color: #fff;
						background: none;
						width: 90%;
						height: 32px;
						.el-range-input  {
				background: none;
			}
			.el-input__icon {
				line-height: 1;
			}
		}
	}
	.echarts3:hover {
			}
	.echarts4 {
				padding: 8px 0 0 0;
				margin: 0;
				flex-direction: column;
				background: none;
				flex: auto;
				display: flex;
				width: 100%;
				transition: 0.3s;
				height: 0;
				::v-deep.querySelect {
			.el-input {
				height: auto
			}
			.el-input__inner,.el-range-input  {
								border: 1px solid #ffffff20;
								padding: 0 5px;
								margin: 5px auto 0 10px;
								z-index: 9;
								color: #fff;
								background: none;
								flex: none;
								width: 90%;
								height: 32px;
							}
			.el-input__icon {
				line-height: 1;
			}
		}
		::v-deep.querySelect2 {
						border: 1px solid #ffffff20;
						padding: 0 5px;
						margin: 5px auto 0 10px;
						z-index: 9;
						color: #fff;
						background: none;
						flex: none;
						width: 90%;
						height: 32px;
						.el-range-input  {
				background: none;
			}
			.el-input__icon {
				line-height: 1;
			}
		}
	}
	.echarts4:hover {
			}
	.echarts5 {
				padding: 8px 0 0 0;
				margin: 0;
				flex-direction: column;
				background: none;
				flex: auto;
				display: flex;
				width: 100%;
				transition: 0.3s;
				height: 0;
				::v-deep.querySelect {
			.el-input {
				height: auto
			}
			.el-input__inner,.el-range-input  {
								border: 1px solid #ffffff20;
								padding: 0 5px;
								margin: 5px auto 0 10px;
								z-index: 9;
								color: #fff;
								background: none;
								width: 90%;
								height: 32px;
							}
			.el-input__icon {
				line-height: 1;
			}
		}
		::v-deep.querySelect2 {
						border: 1px solid #ffffff20;
						padding: 0 5px;
						margin: 5px auto 0 10px;
						z-index: 9;
						color: #fff;
						background: none;
						width: 90%;
						height: 32px;
						.el-range-input  {
				background: none;
			}
			.el-input__icon {
				line-height: 1;
			}
		}
	}
	.echarts5:hover {
			}
	.echarts6 {
				padding: 8px 0 0 0;
				margin: 0;
				flex-direction: column;
				background: none;
				flex: auto;
				display: flex;
				width: 100%;
				transition: 0.3s;
				height: 0;
				::v-deep.querySelect {
			.el-input {
				height: auto
			}
			.el-input__inner,.el-range-input  {
								border: 1px solid #ffffff20;
								padding: 0 5px;
								margin: 5px auto 0 10px;
								z-index: 9;
								color: #fff;
								background: none;
								width: 90%;
								height: 32px;
							}
			.el-input__icon {
				line-height: 1;
			}
		}
		::v-deep.querySelect2 {
						border: 1px solid #ffffff20;
						padding: 0 5px;
						margin: 5px auto 0 10px;
						z-index: 9;
						color: #fff;
						background: none;
						width: 90%;
						height: 32px;
						.el-range-input  {
				background: none;
			}
			.el-input__icon {
				line-height: 1;
			}
		}
	}
	.echarts6:hover {
			}
	.echarts7 {
				padding: 8px 0 0 0;
				margin: 0;
				flex-direction: column;
				background: none;
				flex: auto;
				display: flex;
				width: 100%;
				transition: 0.3s;
				height: 0;
				order: 3;
				::v-deep.querySelect {
			.el-input {
				height: auto
			}
			.el-input__inner,.el-range-input  {
								border: 1px solid #ffffff20;
								padding: 0 5px;
								margin: 5px auto 0 10px;
								z-index: 9;
								color: #fff;
								background: none;
								width: 90%;
								height: 32px;
							}
			.el-input__icon {
				line-height: 1;
			}
		}
		::v-deep.querySelect2 {
						border: 1px solid #ffffff20;
						padding: 0 5px;
						margin: 5px auto 0 10px;
						z-index: 9;
						color: #fff;
						background: none;
						width: 90%;
						height: 32px;
						.el-range-input  {
				background: none;
			}
			.el-input__icon {
				line-height: 1;
			}
		}
	}
	.echarts7:hover {
			}
	::-webkit-scrollbar {
		display: none; /* 针对Webkit浏览器 */
	}
	::v-deepoption {
		color: #000;
	}
</style>

