console.log("bonjour le pentest ")
let myV=document.getElementById("idArt").value
let idUser=document.getElementById("idUser").value
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
                    allCategories{
                        edges{
                        node{
                            id,nom,
                            articleCategorie{
                            edges{
                                node{
                                titre,image,imageSingle,tag {
                                    edges {
                                    node {
                                        id
                                    }
                                    }
                                },
                                categorie{
                                    nom
                                },description,contenu,dateAdd,dateUpd,
                                articleCommentaire{
                                    edges{
                                    node{
                                        user {
                                        id
                                        },message,sujet,dateAdd,dateUpd
                                    }
                                    }
                                },
                                auteur{
                                    username,firstName,email,isStaff,isActive,image,description,
                                    social{
                                    edges{
                                        node{
                                        id,name,lien
                                        }
                                    }
                                    },
                                    specialite{
                                    edges{
                                        node{
                                        id,specialiste
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
                    category(id:"Q2F0ZWdvcmllTm9kZTox"){
                        id,nom, 
                        articleCategorie{
                            edges{
                                node{
                                titre,image,imageSingle,tag {
                                    edges {
                                    node {
                                        id
                                    }
                                    }
                                },
                                categorie{
                                    nom
                                },description,contenu,dateAdd,dateUpd,
                                articleCommentaire{
                                    edges{
                                    node{
                                        user {
                                        id
                                        },message,sujet,dateAdd,dateUpd
                                    }
                                    }
                                },
                                auteur{
                                    username,firstName,email,isStaff,isActive,image,description,
                                    social{
                                    edges{
                                        node{
                                        id,name,lien
                                        }
                                    }
                                    },
                                    specialite{
                                    edges{
                                        node{
                                        id,specialiste
                                        }
                                    }
                                    }
                                }
                                }	
                            }
                        },
                    },
                    allArticles{
                        edges{
                            node{
                                id,titre,image,imageSingle,description,dateAdd,dateUpd,
                                tag{
                                edges{
                                    node{
                                    id,nom
                                    }
                                }
                                            },
                                categorie{
                                nom
                                },
                                articleCommentaire{
                                edges{
                                    node{
                                    user{
                                        id,username
                                    }
                                    ,message,sujet,dateAdd,dateUpd
                                    }
                                }
                    },
                                auteur{
                                username,firstName,email,isStaff,isActive,image,description,
                                social{
                                    edges{
                                    node{
                                        id,name,lien
                                    }
                                    }
                                },
                                specialite{
                                    edges{
                                    node{
                                        id,specialiste
                                    }
                                    }
                                }
                    },contenu
                            }	
                            }
                    },
                    article(id:"QXJ0aWNsZU5vZGU6MQ=="){
                        id,titre,image,imageSingle,description,dateAdd,dateUpd,
                        tag{
                            edges{
                            node{
                                id,nom
                            }
                            }
                        },
                        categorie{
                            nom
                        },
                        articleCommentaire{
                            edges{
                            node{
                                user{
                                id,username
                                }
                                ,message,sujet,dateAdd,dateUpd
                            }
                            }
                    },
                        auteur{
                            username,firstName,email,isStaff,isActive,image,description,
                            social{
                            edges{
                                node{
                                id,name,lien
                                }
                            }
                            },
                            specialite{
                            edges{
                                node{
                                id,specialiste
                                }
                            }
                            }
                    },contenu
                    }
                    }
                    `
                }
            })
            .then(response => {
                result = response.data.data
                console.log(response.data)
                this.dataAllCategory=result.allCategories.edges
                this.categoryId=this.dataAllCategory
                //console.log(this.category)
                this.datAllIngredientesByCategoriy=result.category.ingredients
                //console.log(result)
                console.log(this.dataAllCategory)
                console.log(this.datAllIngredientesByCategoriy)
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