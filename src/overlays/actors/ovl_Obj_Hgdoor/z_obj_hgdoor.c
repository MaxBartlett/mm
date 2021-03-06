#include "z_obj_hgdoor.h"

#define FLAGS 0x00100000

#define THIS ((ObjHgdoor*)thisx)

void ObjHgdoor_Init(Actor* thisx, GlobalContext* globalCtx);
void ObjHgdoor_Destroy(Actor* thisx, GlobalContext* globalCtx);
void ObjHgdoor_Update(Actor* thisx, GlobalContext* globalCtx);
void ObjHgdoor_Draw(Actor* thisx, GlobalContext* globalCtx);

/*
const ActorInit Obj_Hgdoor_InitVars = {
    ACTOR_OBJ_HGDOOR,
    ACTORCAT_PROP,
    FLAGS,
    OBJECT_HGDOOR,
    sizeof(ObjHgdoor),
    (ActorFunc)ObjHgdoor_Init,
    (ActorFunc)ObjHgdoor_Destroy,
    (ActorFunc)ObjHgdoor_Update,
    (ActorFunc)ObjHgdoor_Draw,
};
*/

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Obj_Hgdoor_0x80BD4090/func_80BD4090.asm")

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Obj_Hgdoor_0x80BD4090/func_80BD40D0.asm")

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Obj_Hgdoor_0x80BD4090/ObjHgdoor_Init.asm")

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Obj_Hgdoor_0x80BD4090/ObjHgdoor_Destroy.asm")

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Obj_Hgdoor_0x80BD4090/func_80BD41E8.asm")

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Obj_Hgdoor_0x80BD4090/func_80BD41FC.asm")

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Obj_Hgdoor_0x80BD4090/func_80BD42AC.asm")

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Obj_Hgdoor_0x80BD4090/func_80BD42C0.asm")

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Obj_Hgdoor_0x80BD4090/func_80BD433C.asm")

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Obj_Hgdoor_0x80BD4090/func_80BD4358.asm")

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Obj_Hgdoor_0x80BD4090/func_80BD4460.asm")

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Obj_Hgdoor_0x80BD4090/func_80BD4478.asm")

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Obj_Hgdoor_0x80BD4090/func_80BD44D0.asm")

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Obj_Hgdoor_0x80BD4090/func_80BD4500.asm")

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Obj_Hgdoor_0x80BD4090/ObjHgdoor_Update.asm")

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Obj_Hgdoor_0x80BD4090/ObjHgdoor_Draw.asm")
