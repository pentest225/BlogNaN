var app = new Vue({
    el: '#app',
    data: {
        base_url:'',
        dataAllCategory:[],
        datAllIngredientesByCategoriy:[],
        datSingleCategory:[],
        categoryId:'',
    },
    delimiters:["${","}"],
    mounted(){
        this.getdata()
    },
    methods: {
        reverseMessage: function () {
        this.message = this.message.split('').reverse().join('')
        },
        hello:function(){
            console.log('hello world\r\n')
        },
        getdata: function(){
            this.base_url = '127.0.0.1:8000'
            console.log('data getting')
            axios.defaults.xsrfCookieName = 'csrftoken'
            axios.defaults.xsrfHeaderName = 'X-CSRFToken'
            axios({
                url: 'http://'+this.base_url + '/graphql',
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
    },


    })