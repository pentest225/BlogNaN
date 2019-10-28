var app = new Vue({
    el: '#app',
    data: {
        base_url:'',
        dataAllCategory:[],
        dataAllarticle:[],
        datAllIngredientesByCategoriy:[],
        datSingleCategory:[],
        categoryId:'',
        nom: '',
        sujet: '',
        email: '',
        message: '',
        suscribe:'',
    },
    delimiters:["${","}"],
    mounted(){
        this.getdata()
    },
    methods: {
        getdata: function() {
            this.base_url = 'localhost:8000'
            console.log('data getting')
            axios.defaults.xsrfCookieName = 'csrftoken'
            axios.defaults.xsrfHeaderName = 'X-CSRFToken'
            axios({
                url: 'https://127.0.0.1:8000/graphql',
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
                                        username,firstName,email,isStaff,isActive,image,description,lastName
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
                        allArticles(status:true){
                            edges{
                                node{
                                    id,titre,image,imageSingle,description,dateAdd,dateUpd,isArchive
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
                // console.log(response.data)
                this.dataAllCategory=result.allCategories.edges
                this.categoryId=this.dataAllCategory
                this.dataAllarticle = result.allArticles.edges
                // console.log(this.dataAllCategory)
                console.log(this.dataAllarticle)

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
            axios.post('https://127.0.0.1:8000/contacts/message',formData,
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
            axios.post('https://127.0.0.1:8000/contacts/souscription',formData,
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
    },


    })