<template>
	<div>

		<div class="container" :style="{'backgroundImage': indexBgUrl?`url(${$config.baseUrl + indexBgUrl})`:''}">
			<el-form class='rgs-form animate__animated animate__' v-if="pageFlag=='register'" ref="registerForm" :model="registerForm" :rules="rules">
				<div class="rgs-form2">
					<div class="title">基于Python的网络爬虫与数据可视化分析平台注册</p></div>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="zhanghao">
						<div class="label" :class="changeRules('zhanghao')?'required':''">账号：</div>
						<el-input v-model="registerForm.zhanghao" :readonly="ro.zhanghao" placeholder="请输入账号" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="mima">
						<div class="label" :class="changeRules('mima')?'required':''">密码：</div>
						<el-input v-model="registerForm.mima" type="password" placeholder="请输入密码"  />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="mima2">
						<div class="label" :class="changeRules('mima')?'required':''">确认密码：</div>
						<el-input v-model="registerForm.mima2" type="password" placeholder="请再次输入密码" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="xingming">
						<div class="label" :class="changeRules('xingming')?'required':''">姓名：</div>
						<el-input v-model="registerForm.xingming" :readonly="ro.xingming" placeholder="请输入姓名" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="xingbie">
						<div class="label" :class="changeRules('xingbie')?'required':''">性别：</div>
						<el-select filterable v-model="registerForm.xingbie" placeholder="请选择性别" :disabled="ro.xingbie">
							<el-option
								v-for="(item,index) in yonghuxingbieOptions"
								:key="index"
								:label="item"
								:value="item">
							</el-option>
						</el-select>
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="shouji">
						<div class="label" :class="changeRules('shouji')?'required':''">手机：</div>
						<el-input v-model="registerForm.shouji" :readonly="ro.shouji" placeholder="请输入手机" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="touxiang">
						<div class="label" :class="changeRules('touxiang')?'required':''">头像：</div>
						<file-upload
							tip="点击上传头像"
							action="file/upload"
							:limit="1"
							accept="image/*"
							:multiple="true"
							:fileUrls="registerForm.touxiang?registerForm.touxiang:''"
							@change="yonghutouxiangUploadChange"
						></file-upload>
					</el-form-item>
					<div class="register-btn">
						<div class="register-btn1">
							<el-button class="register_btn" type="primary" @click="submitForm('registerForm')">注册</el-button>
						</div>
						<div class="register-btn2">
							<router-link class="has_btn" to="/login">已有账号，直接登录</router-link>
						</div>
					</div>
				</div>
				<div class="idea1"></div>
				<div class="idea2"></div>
			</el-form>
		</div>
	</div>
</div>
</template>

<script>
	import 'animate.css';

export default {
    //数据集合
    data() {
		return {
            pageFlag : '',
			tableName: '',
			registerForm: {},
			forgetForm: {},
			rules: {},
			ro: {},
			requiredRules: {},
            yonghuxingbieOptions: [],
			indexBgUrl: '',
		}
    },
	mounted() {
		if(this.$route.query.pageFlag=='register'){
			this.tableName = this.$route.query.role;
			if(this.tableName=='yonghu'){
				this.registerForm = {
					zhanghao: '',
					mima: '',
					mima2: '',
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
				this.rules.zhanghao = [{ required: true, message: '请输入账号', trigger: 'blur' }];
				this.requiredRules.zhanghao = [{ required: true, message: '请输入账号', trigger: 'blur' }]
				this.rules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }];
				this.requiredRules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }]
				this.rules.xingming = [{ required: true, message: '请输入姓名', trigger: 'blur' }];
				this.requiredRules.xingming = [{ required: true, message: '请输入姓名', trigger: 'blur' }]
				this.yonghuxingbieOptions = "男,女".split(',');
				this.rules.shouji = [{ required: true, validator: this.$validate.isMobileNotNull, trigger: 'blur' }];
				this.requiredRules.shouji = [{ required: true, message: '请输入手机', trigger: 'blur' }]
				this.rules.status = [{ required: true, validator: this.$validate.isIntNumer, trigger: 'blur' }];
			}
		}
	},
    created() {
		this.$http.get('config/info?name=fRegisterBackgroudImg',).then(rs=>{this.indexBgUrl = rs.data.data?rs.data.data.value:''})
		this.pageFlag = this.$route.query.pageFlag;
    },
    //方法集合
    methods: {
		changeRules(name){
			if(this.requiredRules[name]){
				return true
			}
			return false
		},
		// 获取uuid
		getUUID () {
			return new Date().getTime();
		},
        // 下二随
		yonghutouxiangUploadChange(fileUrls) {
			this.registerForm.touxiang = fileUrls.replace(new RegExp(this.$config.baseUrl,"g"),"");
		},

		// 多级联动参数


		submitForm(formName) {
			this.$refs[formName].validate((valid) => {
				if (valid) {
					var url=this.tableName+"/register";
					if(`yonghu` == this.tableName && this.registerForm.mima!=this.registerForm.mima2) {
						this.$message.error(`两次密码输入不一致`);
						return
					}
					this.$http.post(url, this.registerForm).then(res => {
						if (res.data.code === 0) {
							this.$message({
								message: '注册成功',
								type: 'success',
								duration: 1500,
								onClose: () => {
									this.$router.push('/login');
								}
							});
						} else {
							this.$message.error(res.data.msg);
						}
					});
				} else {
					return false;
				}
			});
		},
		resetForm(formName) {
			this.$refs[formName].resetFields();
		},
    }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.container {
		background-repeat: no-repeat;
		background-size: 100% 100% !important;
		background: url(http://codegen.caihongy.cn/20250815/815abdc262b84ea1a3b38ab3b5cc13a7.jpg);
		display: flex;
		width: 100%;
		min-height: 100vh;
		justify-content: center;
		align-items: center;
		background-position: center center;
		position: relative;
		background: url(http://codegen.caihongy.cn/20250815/815abdc262b84ea1a3b38ab3b5cc13a7.jpg);
		.rgs-form {
			border-radius: 0;
			padding: 40px 40px;
			box-shadow: 0 0px 0px rgba(0, 0, 0, .5);
			margin: 0 auto 0 10%;
			z-index: 10;
			background: rgba(255,255,255,.5);
			width: 600px;
			height: auto;
			.rgs-form2 {
				width: 100%;
				.title {
					margin: 0 0 30px -30%;
					text-shadow: none;
					color: #05441a;
					width: 160%;
					font-size: 24px;
					line-height: 44px;
					text-align: center;
				}
				.subtitle {
					margin: 0 0 10px 0;
					text-shadow: 4px 4px 2px rgba(64, 158, 255, .5);
					color: rgba(64, 158, 255, 1);
					width: 100%;
					font-size: 20px;
					line-height: 44px;
					text-align: center;
				}
				.list-item {
					padding: 0;
					margin: 0 auto 15px;
					width: 100%;
					border-color: #ddd;
					border-width: 1px 0;
					position: relative;
					border-style: dashed;
					height: auto;
					::v-deep .el-form-item__content {
						padding: 0 0 0 120px;
						display: block;
						width: 100%;
						.label {
							padding: 0 5px 0 0;
							z-index: 9;
							color: #05441a;
							left: 0;
							width: 120px;
							font-size: 16px;
							line-height: 40px;
							position: absolute !important;
							text-align: right;
						}
						
						.required {
							position: relative;
						}
						.required::after{
							color: red;
							left: 110px;
							position: absolute;
							content: "*";
						}
						.el-input {
							flex: 1;
							width: 100%;
						}
						.el-input .el-input__inner {
							border: 0;
							border-radius: 0 20px 20px 0;
							padding: 0 10px;
							box-shadow: none;
							outline: none;
							color: #666;
							background: none;
							width: 100%;
							font-size: 14px;
							height: 40px;
						}
						.el-input .el-input__inner:focus {
							border: 0;
							border-radius: 0 20px 20px 0;
							padding: 0 10px;
							box-shadow: none;
							outline: none;
							color: #666;
							background: none;
							width: 100%;
							font-size: 14px;
							height: 40px;
						}
						.el-input-number {
							flex: 1;
							width: 100%;
						}
						.el-input-number .el-input__inner {
							text-align: left;
							border: 0;
							border-radius: 0 20px 20px 0;
							padding: 0 10px;
							box-shadow: none;
							outline: none;
							color: #666;
							background: none;
							width: 100%;
							font-size: 14px;
							height: 40px;
						}
						.el-input-number .el-input-number__decrease {
							display: none;
						}
						.el-input-number .el-input-number__increase {
							display: none;
						}
						.el-select {
							flex: 1;
							width: 100%;
						}
						.el-select .el-input__inner {
							border: 0;
							border-radius: 0 20px 20px 0;
							padding: 0 10px;
							box-shadow: none;
							outline: none;
							color: #666;
							background: none;
							width: 100%;
							font-size: 16px;
							height: 40px;
						}
						.el-select .el-input__inner:focus {
							border: 0;
							border-radius: 0 20px 20px 0;
							padding: 0 10px;
							box-shadow: none;
							outline: none;
							color: #666;
							background: none;
							width: 100%;
							font-size: 16px;
							height: 40px;
						}
						.el-date-editor {
							flex: 1;
							width: 100%;
						}
						.el-date-editor .el-input__inner {
							border: 0;
							border-radius: 0 20px 20px 0;
							padding: 0 10px 0 30px;
							box-shadow: none;
							outline: none;
							color: #666;
							background: none;
							width: 100%;
							font-size: 16px;
							height: 40px;
						}
						.el-date-editor .el-input__inner:focus {
							border: 0;
							border-radius: 0 20px 20px 0;
							padding: 0 10px 0 30px;
							box-shadow: none;
							outline: none;
							color: #666;
							background: none;
							width: 100%;
							font-size: 16px;
							height: 40px;
						}
						.el-upload--picture-card {
							background: transparent;
							border: 0;
							border-radius: 0;
							width: auto;
							height: auto;
							line-height: initial;
							vertical-align: middle;
						}
						.upload .upload-img {
							border: 1px solid #eee;
							cursor: pointer;
							border-radius: 0;
							margin: 10px 0 0 0;
							color: #999;
							background: rgba(255,255,255,.5);
							object-fit: cover;
							width: 60px;
							font-size: 22px;
							line-height: 60px;
							text-align: center;
							height: 60px;
						}
						.el-upload-list .el-upload-list__item {
							border: 1px solid #eee;
							cursor: pointer;
							border-radius: 0;
							margin: 10px 0 0 0;
							color: #999;
							background: rgba(255,255,255,.5);
							object-fit: cover;
							width: 60px;
							font-size: 22px;
							line-height: 60px;
							text-align: center;
							height: 60px;
							font-size: 14px;
							line-height: 1.8;
						}
						.el-upload .el-icon-plus {
							border: 1px solid #eee;
							cursor: pointer;
							border-radius: 0;
							margin: 10px 0 0 0;
							color: #999;
							background: rgba(255,255,255,.5);
							object-fit: cover;
							width: 60px;
							font-size: 22px;
							line-height: 60px;
							text-align: center;
							height: 60px;
						}
						.el-upload__tip {
							margin: 0;
							color: #333;
							font-size: 15px;
						}
						.emailInput {
							border: 0;
							border-radius: 0 20px 20px 0;
							padding: 0 10px;
							box-shadow: none;
							margin: 0;
							outline: none;
							color: #666;
							background: none;
							flex: 1;
							width: 100%;
							font-size: 14px;
							height: 40px;
						}
						.emailInput:focus {
							border: 0;
							border-radius: 0 20px 20px 0;
							padding: 0 10px;
							box-shadow: none;
							outline: none;
							color: #666;
							flex: 1;
							background: none;
							width: 100%;
							font-size: 16px;
							height: 40px;
						}
						.el-btn {
							border: 0;
							cursor: pointer;
							padding: 0 15px;
							margin: 5px 0;
							color: #05441a;
							font-size: 15px;
							float: right;
							border-radius: 0 0px 0px 0;
							box-shadow: 0 0 0px rgba(64, 158, 255, .5);
							outline: none;
							background: #05441a20;
							width: auto;
							height: 40px;
						}
						.el-btn:hover {
							opacity: 0.8;
						}
						
						.el-input__inner::placeholder {
							color: #123;
							font-size: 16px;
						}
						input::placeholder {
							color: #123;
							font-size: 16px;
						}
						.editor {
							margin: 10px 0;
							background: #fff;
							width: 100%;
							height: auto;
						}
						.editor .ql-toolbar {
							background: none;
						}
						.editor .ql-container {
							background: none;
						}
						.editor .ql-container .ql-blank::before {
							color: #000;
						}
					}
				}
				.register-btn {
					padding: 0;
					margin: 30px 0 0;
					width: 100%;
					text-align: center、;
				}
				.register-btn1 {
					margin: 0 20px 0 0;
					display: inline-block;
					width: 100%;
					text-align: center;
				}
				.register-btn2 {
					display: inline-block;
					width: 100%;
					text-align: right;
				}
				.register_btn {
					border: 0;
					cursor: pointer;
					padding: 0 30px;
					margin: 0 auto 10px;
					color: #fff;
					font-size: 18px;
					line-height: 40px;
					transition: all 0s;
					border-radius: 0px;
					outline: none;
					background: #0e5b28;
					width: 100%;
					min-width: 120px;
					height: auto;
				}
				.register_btn:hover {
					opacity: 0.8;
				}
				.has_btn {
					cursor: pointer;
					padding: 0;
					color: #666;
					display: inline-block;
					text-decoration: underline;
					font-size: 16px;
					line-height: 30px;
				}
				.has_btn:hover {
					text-decoration: underline;
					opacity: 1;
				}
			}
			.idea1 {
				background: red;
				display: none;
				width: 100%;
				height: 40px;
			}
			.idea2 {
				background: blue;
				display: none;
				width: 100%;
				height: 40px;
			}
		}
	}
	
	::-webkit-scrollbar {
		display: none;
	}
</style>
