<template>
	<div>
		<div class="register-container" :style="{'backgroundImage': indexBgUrl?`url(${$base.url + indexBgUrl})`:''}">
			<el-form v-if="pageFlag=='register'" ref="ruleForm" class="rgs-form animate__animated animate__" :model="ruleForm" :rules="rules">
				<div class="rgs-form2">
					<div class="title">基于Python的网络爬虫与数据可视化分析平台注册</div>
					<el-form-item class="list-item" v-if="tableName=='yonghu'">
						<div class="lable" :class="changeRules('zhanghao')?'required':''">账号：</div>
						<el-input  v-model="ruleForm.zhanghao" :readonly="ro.zhanghao" autocomplete="off" placeholder="账号"  type="text"  />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'">
						<div class="lable" :class="changeRules('mima')?'required':''">密码：</div>
						<el-input  v-model="ruleForm.mima" :readonly="ro.mima" autocomplete="off" placeholder="密码"  type="password"  />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'">
						<div class="lable" :class="changeRules('mima')?'required':''">确认密码：</div>
						<el-input  v-model="ruleForm.mima2" autocomplete="off" placeholder="确认密码" type="password" :readonly="ro.mima" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'">
						<div class="lable" :class="changeRules('xingming')?'required':''">姓名：</div>
						<el-input  v-model="ruleForm.xingming" :readonly="ro.xingming" autocomplete="off" placeholder="姓名"  type="text"  />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'">
						<div class="lable" :class="changeRules('xingbie')?'required':''">性别：</div>
						<el-select filterable v-model="ruleForm.xingbie" placeholder="请选择性别" :disabled="ro.xingbie">
							<el-option
								v-for="(item,index) in yonghuxingbieOptions"
								:key="index"
								:label="item"
								:value="item">
							</el-option>
						</el-select>
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'">
						<div class="lable" :class="changeRules('shouji')?'required':''">手机：</div>
						<el-input  v-model="ruleForm.shouji" :readonly="ro.shouji" autocomplete="off" placeholder="手机"  type="text"  />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'">
						<div class="lable" :class="changeRules('touxiang')?'required':''">头像：</div>
						<file-upload
							tip="点击上传头像"
							action="file/upload"
							:limit="3"
							accept="image/*"
							:multiple="true"
							:fileUrls="ruleForm.touxiang?ruleForm.touxiang:''"
							@change="yonghutouxiangUploadChange"
						></file-upload>
					</el-form-item>
					<div class="register-btn">
						<div class="register-btn1">
							<button type="button" class="r-btn" @click="login()">注册</button>
						</div>
						<div class="register-btn2">
							<div class="r-login" @click="close()">取消</div>
						</div>
					</div>
				</div>
			</el-form>
		</div>
	</div>
</template>

<script>
	import 'animate.css'
export default {
	data() {
		return {
			ruleForm: {
			},
			forgetForm: {},
            pageFlag : '',
			tableName:"",
			rules: {},
			ro: {},
            yonghuxingbieOptions: [],
			indexBgUrl: '',
		};
	},
	mounted(){
		this.pageFlag = this.$route.query.pageFlag
		if(this.$route.query.pageFlag=='register'){
			
			let table = this.$storage.get("loginTable");
			this.tableName = table;
			if(this.tableName=='yonghu'){
				this.ruleForm = {
					zhanghao: '',
					mima: '',
					xingming: '',
					xingbie: '',
					shouji: '',
					touxiang: '',
					status: '',
				}
				this.ro = {
					zhanghao: false,
					mima: false,
					xingming: false,
					xingbie: false,
					shouji: false,
					touxiang: false,
					status: false,
				}
			}
			if ('yonghu' == this.tableName) {
				this.rules.zhanghao = [{ required: true, message: '请输入账号', trigger: 'blur' }]
			}
			if ('yonghu' == this.tableName) {
				this.rules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }]
			}
			if ('yonghu' == this.tableName) {
				this.rules.xingming = [{ required: true, message: '请输入姓名', trigger: 'blur' }]
			}
			if ('yonghu' == this.tableName) {
				this.rules.shouji = [{ required: true, message: '请输入手机', trigger: 'blur' }]
			}
			this.yonghuxingbieOptions = "男,女".split(',')
		}
	},
	created() {
		this.$http.get('config/info?name=bRegisterBackgroundImg',).then(rs=>{this.indexBgUrl = rs.data.data?rs.data.data.value:''})
	},
	destroyed() {
		  	},
	methods: {
		changeRules(name){
			if(this.rules[name]){
				return true
			}
			return false
		},
		// 获取uuid
		getUUID () {
			return new Date().getTime();
		},
		close(){
			this.$router.push({ path: "/login" });
		},
        yonghutouxiangUploadChange(fileUrls) {
            this.ruleForm.touxiang = fileUrls;
        },

        // 多级联动参数


		// 注册
		login() {
			var url=this.tableName+"/register";
			if((!this.ruleForm.zhanghao) && `yonghu` == this.tableName){
				this.$message.error(`账号不能为空`);
				return
			}
			if((!this.ruleForm.mima) && `yonghu` == this.tableName){
				this.$message.error(`密码不能为空`);
				return
			}
			if((this.ruleForm.mima!=this.ruleForm.mima2) && `yonghu` == this.tableName){
				this.$message.error(`两次密码输入不一致`);
				return
			}
			if((!this.ruleForm.xingming) && `yonghu` == this.tableName){
				this.$message.error(`姓名不能为空`);
				return
			}
			if((!this.ruleForm.shouji) && `yonghu` == this.tableName){
				this.$message.error(`手机不能为空`);
				return
			}
			if(`yonghu` == this.tableName && this.ruleForm.shouji &&(!this.$validate.isMobile(this.ruleForm.shouji))){
				this.$message.error(`手机应输入手机格式`);
				return
			}
            if(this.ruleForm.touxiang!=null) {
                this.ruleForm.touxiang = this.ruleForm.touxiang.replace(new RegExp(this.$base.url,"g"),"");
            }
			this.$http({
				url: url,
				method: "post",
				data:this.ruleForm
			}).then(({ data }) => {
				if (data && data.code === 0) {
					this.$message({
						message: "注册成功",
						type: "success",
						duration: 1500,
						onClose: () => {
							this.$router.replace({ path: "/login" });
						}
					});
				} else {
					this.$message.error(data.msg);
				}
			});
		},
	}
};
</script>

<style lang="scss" scoped>
.register-container {
	position: relative;
	background: url(http://codegen.caihongy.cn/20250906/6759760eab6d436baf1714deb0fa1dae.png);
	background-repeat: no-repeat;
	background-size: cover !important;
	background: url(http://codegen.caihongy.cn/20250906/6759760eab6d436baf1714deb0fa1dae.png);
	display: flex;
	width: 100%;
	min-height: 100vh;
	justify-content: center;
	align-items: center;
	background-position: center bottom;
	.rgs-form {
		.rgs-form2 {
		padding: 122px 40px 10px 130px;
		margin: 0  153px 0 0;
		background: rgba(255,255,255,.6);
		display: flex;
		width: 600px;
		position: relative;
		flex-wrap: wrap;
		}
		border-radius: 0;
		padding: 0;
		margin: 30px auto;
		z-index: 1;
		flex-direction: column;
		background: none;
		display: flex;
		width: 100%;
		align-items: flex-end;
		flex-wrap: wrap;
		height: auto;
		.title {
			padding: 0 10px;
			margin: 0px 0 20px 0;
			color: #0D1818;
			font-weight: 600;
			display: flex;
			font-size: 22px;
			line-height: 33px;
			text-shadow: none;
			top: 0;
			align-content: center;
			left: 0;
			background: #F1D36D;
			width: 100%;
			justify-content: center;
			align-items: center;
			position: absolute;
			text-align: center;
			height: 92px;
		}
		.list-item {
			box-shadow:  inset 0px 3px 6px 1px rgba(0,0,0,0.16);
			margin: 0  30px 20px;
			background: none;
			width: 100%;
			position: relative;
			height: auto;
			::v-deep .el-form-item__content {
				display: block;
			}
			.lable {
				padding: 0 10px 0 0;
				color: #333;
				left: -130px;
				width: 130px;
				font-size: 16px;
				line-height: 60px;
				position: absolute !important;
				text-align: right;
			}
			.el-input {
				width: 100%;
			}
			.el-input ::v-deep .el-input__inner {
				border: 0px solid #DADFE6;
				border-radius: 4px;
				padding: 0 10px;
				color: #333;
				background: none;
				width: 100%;
				font-size: 16px;
				height: 44px;
			}
			.el-input ::v-deep .el-input__inner:focus {
				border: 0px solid #DADFE6;
				border-radius: 4px;
				padding: 0 10px;
				color: #333;
				background: none;
				width: 100%;
				font-size: 16px;
				height: 44px;
			}
			.el-input-number {
				width: 100%;
			}
			.el-input-number ::v-deep .el-input__inner {
				text-align: center;
				border: 0px solid #DADFE6;
				border-radius: 4px;
				padding: 0 10px;
				color: #333;
				background: none;
				width: 100%;
				font-size: 16px;
				height: 44px;
			}
			.el-input-number ::v-deep .el-input__inner:focus {
				border: 0px solid #DADFE6;
				border-radius: 4px;
				padding: 0 10px;
				color: #333;
				background: none;
				width: 100%;
				font-size: 16px;
				height: 44px;
			}
			.el-input-number ::v-deep .el-input-number__decrease {
				display: none;
			}
			.el-input-number ::v-deep .el-input-number__increase {
				display: none;
			}
			.el-select {
				width: 100%;
			}
			.el-select ::v-deep .el-input__inner {
				border: 0px solid #DADFE6;
				border-radius: 4px;
				padding: 0 10px;
				color: #666;
				background: none;
				width: 100%;
				font-size: 16px;
				height: 44px;
			}
			.el-select ::v-deep .el-input__inner:focus {
				border: 0px solid #DADFE6;
				border-radius: 4px;
				padding: 0 10px;
				color: #666;
				background: none;
				width: 100%;
				font-size: 16px;
				height: 44px;
			}
			.el-date-editor {
				width: 100%;
			}
			.el-date-editor ::v-deep .el-input__inner {
				border: 0px solid #DADFE6;
				border-radius: 4px;
				padding: 0 30px;
				color: #666;
				background: none;
				width: 100%;
				font-size: 16px;
				height: 44px;
			}
			.el-date-editor ::v-deep .el-input__inner:focus {
				border: 0px solid #DADFE6;
				border-radius: 4px;
				padding: 0 30px;
				color: #333;
				background: none;
				width: 100%;
				font-size: 16px;
				height: 44px;
			}
			.el-date-editor.el-input {
				width: 100%;
			}
			::v-deep .el-upload--picture-card {
				background: transparent;
				border: 0;
				border-radius: 0;
				width: auto;
				height: auto;
				line-height: initial;
				vertical-align: middle;
			}
			::v-deep .upload .upload-img {
				border: 0px solid #ddd;
				cursor: pointer;
				border-radius: 4px;
				margin: 0px 0 0;
				color: #999;
				width: 90px;
				font-size: 26px;
				line-height: 60px;
				text-align: center;
				height: 60px;
			}
			::v-deep .el-upload-list .el-upload-list__item {
				border: 0px solid #ddd;
				cursor: pointer;
				border-radius: 4px;
				margin: 0px 0 0;
				color: #999;
				width: 90px;
				font-size: 26px;
				line-height: 60px;
				text-align: center;
				height: 60px;
			}
			::v-deep .el-upload .el-icon-plus {
				border: 0px solid #ddd;
				cursor: pointer;
				border-radius: 4px;
				margin: 0px 0 0;
				color: #999;
				width: 90px;
				font-size: 26px;
				line-height: 60px;
				text-align: center;
				height: 60px;
			}
			::v-deep .el-upload__tip {
				margin: 0 0 0 20px;
				color: #666;
				font-size: 16px;
			}
			::v-deep .el-input__inner::placeholder {
				color: #999;
				font-size: 16px;
			}
			.required {
				position: relative;
			}
			.required::after{
				color: red;
				left: 120px;
				position: absolute;
				content: "*";
			}
			.editor {
				border: 0;
				width: 100%;
				height: auto;
			}
			.editor>.avatar-uploader {
				line-height: 0;
				height: 0;
			}
		}
		.list-item.email {
			input {
				border: 0px solid #DADFE6;
				border-radius: 4px 0 0 4px;
				padding: 0 10px;
				color: #333;
				flex: 1;
				background: none;
				width: 100%;
				font-size: 16px;
				height: 44px;
			}
			input:focus {
				border: 0px solid #DADFE6;
				border-radius: 4px 0 0 4px;
				padding: 0 10px;
				color: #333;
				flex: 1;
				background: none;
				width: 100%;
				font-size: 16px;
				height: 44px;
			}
			input::placeholder {
				color: #999;
				font-size: 16px;
			}
			button {
				border: 0;
				cursor: pointer;
				padding: 0 10px;
				margin: 0;
				color: #fff;
				font-size: 16px;
				border-color: #d1d1d1;
				border-radius: 0 4px 4px 0;
				box-shadow: none;
				outline: none;
				background: #10C17C;
				width: 130px;
				border-width: 0 0 0px;
				border-style: solid;
				height: 44px;
			}
			button:hover {
				color: #4c7bf5;
				border-color: #4c7bf5;
			}
		}
		.register-btn {
			display: flex;
			width: 100%;
			justify-content: center;
			flex-wrap: wrap;
		}
		.register-btn1 {
			margin: 0 20px 0 0;
			width: auto;
		}
		.register-btn2 {
			width: 176px;
		}
		.r-btn {
			border: 0;
			cursor: pointer;
			border-radius: 24px;
			outline: none;
			color: #fff;
			background: #10C17C;
			font-weight: bold;
			width: 176px;
			font-size: 16px;
			height: 47px;
		}
		.r-btn:hover {
			opacity: 0.5;
		}
		.r-login {
			border: 0;
			cursor: pointer;
			padding: 0 24px;
			margin: 0 0 20px;
			color: #333333;
			font-weight: bold;
			font-size: 16px;
			line-height: 47px;
			border-radius: 24px;
			outline: none;
			background: #FAFAFA;
			width: 176px;
			text-align: center;
			height: 47px;
		}
		.r-login:hover {
			opacity: 0.8;
		}
	}
}
	
	::-webkit-scrollbar {
	  display: none;
	}
</style>
