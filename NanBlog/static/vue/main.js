var app = new Vue({
    el: '#app',
    data: {
        base_url:'',
        dataAllCategory:[],
        dataAllarticle:[],
        datAllIngredientesByCategoriy:[],
        datSingleCategory:[],
        singleAtircle:[],
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
    },
    delimiters:["${","}"],
    mounted(){
        this.idcat="{{idcat}}";
        this.idart="{{idart}}";
        this.getdata()
    },
    methods: {
        getdata: function() {
            this.base_url = 'https://127.0.0.1:8000'
            console.log('data getting')
            axios.defaults.xsrfCookieName = 'csrftoken'
            axios.defaults.xsrfHeaderName = 'X-CSRFToken'
            console.log(this.idcat)
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
                        category(id:"Q2F0ZWdvcmllTm9kZTox"){
                            id,nom, 
                            articleCategorie{
                                edges{
                                    node{
                                    id,titre,image,imageSingle,tag {
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
                                            id,image,lastName,firstName
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
                                            id,username,image,lastName,firstName
                                        },
                                          response{
                                            edges{
                                              node{
                                                user{
                                                  id,firstName,lastName,image
                                                }
                                              }
                                            }
                                          },
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
                        },
                                      articleLike{
                                      edges{
                                        node{
                                          user{
                                            id,lastName,firstName,image
                                          }
                                        }
                                      }
                                    },
                                  contenu
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
                                nom,id
                            },
                            articleCommentaire{
                                edges{
                                node{
                                    user{
                                        id,username,lastName,firstName,image
                                    },
                                  	response{
                                      edges{
                                        node{
                                          user{
                                            lastName,firstName,id,image,
                                          }
                                          message,
                                        }
                                        
                                      }
                                    }
                                    message,sujet,dateAdd,dateUpd
                                  
                                }
                                }
                        },
    												articleLike{
                              edges{
                                node{
                                  user{
                                    id,lastName,firstName,
                                  }
                                }
                              }
                            }
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
                // console.log(response.data)
                this.dataAllCategory = result.allCategories.edges
                this.categoryId=result.category
                this.dataAllarticle = result.allArticles.edges
                this.categoryId=result.category
                this.singleAtircle  = result.article
                this.CarouselAll = this.dataAllarticle.slice(1, 4)
                // this.categoryId =
                console.log(this.idcat)
                console.log(this.CarouselAll)
                // console.log(this.categoryId)
                console.log(this.singleAtircle)
                

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