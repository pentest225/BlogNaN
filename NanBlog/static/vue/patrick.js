console.log("bonjour le pentest ")
// let myV=document.getElementById("idArt").value
// let idUser=document.getElementById("idUser").value

Vue.component('comment_user',{
    delimiters:["${","}"],
    template:`
    <div class="au-message__item unread">
        <div class="au-message__item-inner">
            <div class="au-message__item-text">
                <div class="avatar-wrap">
                    <div class="avatar">
                        <img :src="+'https://localhost:8000/'+ item.node.user.image " alt="John Smith">
                    </div>
                </div>
                <div class="text" >
                    <h5 class="name" >`+" ${item.node.user.username} ${item.node.user.image} "+`</h5>
                    <p id="penComment" v-html="item.node.message"></p>
                </div>
            </div>
            <div class="au-message__item-time">
                <span>`+" ${item.node.dateAdd} "+`</span>
            </div>
        </div>
    </div>
    `,
    props:['item']
})
var app = new Vue({
    el: '#app',
    data: {
        base_url:'',
        dataAllCategory:[],
        datAllIngredientesByCategoriy:[],
        datSingleCategory:[],
        categoryId:'',
        nom: '',
        sujet: '',
        email: '',
        message: '',
        suscribe:'',
        patrick:'Test Patrick',
        articleActive:true,
        idArticle:'',
        idUser:null,
        actionFrom:'',
        myCom:'bonbhhh',
        commentText:'',
        lastArticle:[],
        listeComment:[],
        UserName:document.getElementById('UserName').value
    },
    delimiters:["${","}"],
    mounted(){
        this.getdata()
    },
    methods: {
        getdata: function(){
            this.base_url = 'localhost:8000'
            console.log('data getting')
            axios.defaults.xsrfCookieName = 'csrftoken'
            axios.defaults.xsrfHeaderName = 'X-CSRFToken'
            axios({
                url: 'https://'+this.base_url + '/graphql',
                method: 'post',
                data: {
                    query: `
                    query{
  
                        allUser(username:"admin"){
                            edges{
                            node{
                                id,username,lastName,firstName,image,email,
                                specialite{edges{
                                node{
                                    specialiste,
                                },
                                },
                                },social{
                                edges{
                                    node{
                                    id,name,lien
                                    }
                                }
                                },articleAuteur{
                                edges{
                                    node{
                                    id,titre,description,image,contenu,isArchive,imageSingle,dateAdd,dateUpd,status,
                                    articleCommentaire{
                                        edges{
                                        node{
                                            id,message,sujet,status,dateAdd,dateUpd,
                                            user{
                                                username,firstName,lastName,image,email,
                                            specialite{edges{
                                                            node{
                                                            specialiste,
                                                            },
                                                        },
                                            },social{
                                                    edges{
                                                        node{
                                                        id,name,lien
                                                        }
                                                    }
                                                    }
                                            }
                                        }
                                        }
                                    }
                                    }
                                }
                                }
                            },
                            }
                        }
                        }
                    `
                }
            })
            .then(response => {
                result = response.data.data
                console.log(response.data)
                this.lastArticle=result.allUser.edges[0].node.articleAuteur.edges[0]
                this.listeComment=this.lastArticle.node.articleCommentaire.edges
                console.log("#####################")
                console.log(this.listeComment)
            })  
            .catch((err) => {
                console.log(err);
            })
        },
        sendmessage: function () {
            axios.defaults.xsrfCookieName = 'csrftoken'
            axios.defaults.xsrfHeaderName = 'X-CSRFToken'
            let formData = new FormData();
            formData.append('nom', '' + this.nom);
            formData.append('sujet', '' + this.sujet);
            formData.append('email', '' + this.email);
            formData.append('message', '' + this.message);
            axios.post('http://127.0.0.1:8000/contacts/message',formData,
            {
            } ).then(response => {
                    console.log(response)
                    if (response.data.succes == true) {
                        new Toast({
                            message: 'Votre Message a été envoyé avec Success',
                            type: 'success'
                        });
                        this.nom = ''
                        this.message = ''
                        this.email = ''
                        this.sujet = ''
                    }else{
                        swal("Tous les champs Sont requis", "", "error");
                    }
                    
                })
                .catch((err) => {
                    console.log(err);
                })
        },
        suscription: function () {
            axios.defaults.xsrfCookieName = 'csrftoken'
            axios.defaults.xsrfHeaderName = 'X-CSRFToken'
            let formData = new FormData();
            formData.append('suscribe', '' + this.suscribe);
            axios.post('https://localhost:8000/contacts/souscription',formData,
            {
            } ).then(response => {
                    
                    console.log(response)
                    if (response.data.succes == true) {
                        swal("Merci d'avoir Souscrire au Service Newlestter", "", "success");
                        this.email = ''

                    }else{
                        swal("Entrer Votre adresse Mail pour Souscrire Au service Newlestter de nan blog", "", "error");
                    }
                    
                })

                .catch((err) => {
                    console.log(err);
                })
        },
        testFunction:function(){
            this.actionFrom="modifStatus"
            this.idArticle=myV
            axios.defaults.xsrfCookieName = 'csrftoken'
                axios.defaults.xsrfHeaderName = 'X-CSRFToken'
                axios.post('https://localhost:8000/updateArticle', {
                    action: '' + this.actionFrom,
                    id: '' + this.idArticle,
                    }).then(response => {
                        console.log(response) 
                        if(response.data.success){
                            this.isSuccess=true
                            this.error=false
                            this.messageRes=response.data.message
                        }
                        else{
                            this.error=true
                            this.isSuccess=false
                            this.messageRes=response.data.message
                        }
                        this.isregister=false
                        console.log("success variable"+this.isSuccess)
                        console.log("success variable"+this.error)
                    })
                    .catch((err) => {
                        console.log(err);
                        this.isregister=false
                    })
            },
        sendComment:function(){
            this.actionFrom="addContent"
            this.idArticle=myV
            this.idUser=idUser

            axios.defaults.xsrfCookieName = 'csrftoken'
                axios.defaults.xsrfHeaderName = 'X-CSRFToken'
                axios.post('https://localhost:8000/updateArticle', {
                    action: '' + this.actionFrom,
                    idArticle: '' + this.idArticle,
                    idUser:''+this.idUser,
                    comment:''+this.myCom,
                    }).then(response => {
                        console.log(response) 
                        if(response.data.addCommentOk){
                            swal("Cemment add ", "", "success");
                        }
                        else{
                            this.error=true
                            this.isSuccess=false
                            this.messageRes=response.data.message
                        }
                        this.isregister=false
                        console.log("success variable"+this.isSuccess)
                        console.log("success variable"+this.error)
                    })
                    .catch((err) => {
                        console.log(err);
                        this.isregister=false
                    })
            },

    },


    })