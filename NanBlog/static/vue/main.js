console.log("bonjour le monde ")
var app = new Vue({
    el: '#app',
    data: {
        base_url:'',
        dataAllCategory:[],
        dataAllarticle:[],
        datAllIngredientesByCategoriy:[],
        datSingleCategory:[],
        First:[],
        categoryId:'',
        CarouselAll:[],
        idcat :'',
        idart:'',
        nom: '',
        sujet: '',
        email: '',
        message: '',
        suscribe:'',
        base_url:'',
        patrick:'test patrick',
    },
    delimiters:["${","}"],
    mounted(){
        this.idcat = "{{ idcat }}"
        // this.idart = "{{ idart }}"

        this.getdata()
    },
    methods: {
        getdata: function() {
            this.base_url = 'https://localhost:8000/'
            axios.defaults.xsrfCookieName = 'csrftoken'
            axios.defaults.xsrfHeaderName = 'X-CSRFToken'
            axios({
                url: this.base_url + '/graphql',
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
                            }
                        }
                        }
                    },
                    category(id:"${ this.idcat }"){
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
                                    lastName,username,firstName,email,isStaff,isActive,image,description
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
                    },contenu
                            }	
                            }
                    },
                    article(id:"${ this.idart }"){
                        id,titre,image,imageSingle,description,dateAdd,dateUpd,
                        tag{
                            edges{
                            node{
                                id,nom
                            }
                            }
                        },
                        categorie{
                            nom,id
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
                            lastName,username,firstName,email,isStaff,isActive,image,description,
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
                console.log(result)
                // this.dataAllCategory = result.allCategories.edges
                // this.categoryId=result.category
                // this.dataAllarticle = result.allArticles.edges
                // this.categoryId =
                console.log(this.idcat)

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
            axios.post('https://localhost:8000/contacts/message',formData,
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
    },


    })